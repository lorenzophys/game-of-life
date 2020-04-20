from settings import *
import pygame, sys, numpy


class GameOfLife:
    def __init__(self, drag_mode=True):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Game of life")
        self.color = PINK
        self.background = WHITE
        self.drag_mode = drag_mode #drawing by dragging or point by point
        self.is_running = True
        self.is_drawing =True
        self.mouse_position = None
        self.grid = numpy.array([0 for _ in range(N*N)]).reshape(N, N)


    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False
                self.is_drawing = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.is_drawing = False
            if self.drag_mode:
                if pygame.mouse.get_pressed()[0] and (self.is_drawing == True) and self.mouse_inside_grid():
                    self.mouse_position = pygame.mouse.get_pos()
                    if self.mouse_inside_grid():
                        x, y = self.get_cell_clicked()
                        self.grid[x,y] = 1
                        pygame.display.update()
                    else:
                        break
            else:
                if (event.type == pygame.MOUSEBUTTONDOWN) and (self.is_drawing == True) and self.mouse_inside_grid():
                    x, y = self.get_cell_clicked()
                    self.grid[x,y] = 1 if not(self.grid[x,y]) else  0
    

    def main(self):
        while self.is_running:
            while self.is_drawing:
                self.check_events()
                self.draw_init(self.window, self.grid, self.color, self.background)
                self.mouse_position = pygame.mouse.get_pos()
                pygame.display.update()
                
            self.check_events()
            self.draw_and_update(self.window, self.grid, self.color, self.background)
            pygame.display.update()
            self.clock.tick(FPS)

        pygame.quit()
        sys.exit()


    def draw_and_update(self, window, grid, color, background):
        window.fill(background)

        #Rendering
        pygame.draw.rect(window, color, (OFFSET, OFFSET, WIDTH-2*OFFSET, HEIGHT-2*OFFSET), 2)
        for i in range(1,N):
            pygame.draw.line(window, color, (OFFSET, OFFSET+i*SPACING), (HEIGHT-OFFSET, OFFSET+i*SPACING), 0)
            pygame.draw.line(window, color, (OFFSET+i*SPACING, OFFSET), (OFFSET+i*SPACING, WIDTH-OFFSET), 0)

        #Rules and grid update
        copied_grid = grid.copy()
        for i in range(N):
            for j in range(N):
                if grid[i,j]:
                    pygame.draw.rect(window, color, (OFFSET+j*SPACING, OFFSET+i*SPACING, SPACING, SPACING))

                neighbors = list()
                for x in range(max(0,i-1), min(i+2, N)):
                    for y in range(max(0,j-1), min(j+2,N)):
                            neighbors.append(grid[x,y])
                
                s = (sum(neighbors)-1) if grid[i,j] else sum(neighbors)

                if grid[i,j]:
                    if (s < 2) or (s > 3):
                        copied_grid[i,j] = 0
                else:
                    if s == 3:
                        copied_grid[i,j] = 1

        grid[:] = copied_grid[:]


    def mouse_inside_grid(self):
        if self.mouse_position[0] < OFFSET or self.mouse_position[1] < OFFSET:
            return False
        elif self.mouse_position[0] > SPACING*(N+2) or self.mouse_position[1] > SPACING*(N+2):
            return False
        else:
            return True


    def get_cell_clicked(self):
        if self.mouse_inside_grid():
            x_cell = int((self.mouse_position[0]-OFFSET)//SPACING)
            y_cell = int((self.mouse_position[1]-OFFSET)//SPACING)
            return (y_cell, x_cell)
        else:
            return None


    def draw_init(self, window, grid, color, background):
        window.fill(background)

        #Rendering
        pygame.draw.rect(window, color, (OFFSET, OFFSET, WIDTH-2*OFFSET, HEIGHT-2*OFFSET), 2)
        for i in range(1,N):
            pygame.draw.line(window, color, (OFFSET, OFFSET+i*SPACING), (HEIGHT-OFFSET, OFFSET+i*SPACING), 1)
            pygame.draw.line(window, color, (OFFSET+i*SPACING, OFFSET), (OFFSET+i*SPACING, WIDTH-OFFSET), 1)
        
        for i in range(N):
            for j in range(N):
                if grid[i,j]:
                    pygame.draw.rect(window, color, (OFFSET+j*SPACING, OFFSET+i*SPACING, SPACING, SPACING))

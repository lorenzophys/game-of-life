from settings import *
import pygame, sys, numpy


class GameOfLife:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Game of life")
        self.is_running = True
        self.color = GREEN
        self.background = BLACK
        self.cells = (1,0)
        self.grid = numpy.random.choice(self.cells, N*N, p=[0.5,0.5]).reshape(N, N)


    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False

    
    def main(self):
        while self.is_running:
            self.check_events()
            self.draw_and_update(self.window, self.grid, self.color, self. background)

            pygame.display.update()
            self.clock.tick(FPS)

        pygame.quit()
        sys.exit()


    def draw_and_update(self, window, grid, color, background):
        window.fill(background)

        #Rendering, if you want to see the grid change 0-->1 in pygame.draw.line
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
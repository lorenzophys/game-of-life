# Conway's Game of Life
## What's that?
The **Game of Life**, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970. It is a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input. One interacts with the Game of Life by creating an initial configuration and observing how it evolves. It is Turing complete and can simulate a universal constructor or any other Turing machine. [Wiki][wiki]

## How to use it?
There are two ways you can play Conway's Game of Life: 
1. Run */random-game/main.py* and observe the evolution of a random configuration.  
![alt text](http://g.recordit.co/4jRpUoUtYu.gif "Random")

2. Run */draw-your-own/main.py* and draw the with the the mouse, then press the Spacebar to evolve. By default you draw on the grid by click-dragging. To draw point-by-point set `game = GameOfLife(drag_mode=False)`.  
![alt text](http://g.recordit.co/eTtztXktsQ.gif "Draw")

## Requirements
Python version: 3  
Libraries: pygame, numpy

## License
This project is licensed under the **MIT License** - see the *LICENSE.md* file for details

[wiki]: https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life

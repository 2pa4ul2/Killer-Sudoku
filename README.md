# Killer Sudoku Solver

## Description

This Python program provides a solver for Killer Sudoku puzzles. Killer Sudoku is a variant of Sudoku that includes cages, where groups of cells must sum up to specific values, adding an additional layer of complexity to the puzzle.

The repository have 3 algorithm for solving sudoku algorithm
- **Backjumping**
- **Backtracking**
- **Simulated Annealing**
## Features

- Solve Killer Sudoku puzzles with ease.
- Choose between two solving algorithms: backtracking and backjumping.
- Input cage configurations directly into the program.
- Get detailed information about the solved puzzle, including the placement of numbers and cage configurations.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
  - [Input Cage Configurations](#input-cage-configurations)
  - [Choose Solving Algorithm](#choose-solving-algorithm)
  - [Run the Program](#run-the-program)
- [Examples](#examples)
- [Dependencies](#dependencies)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/killer-sudoku-solver.git
   ```

2. Navigate to the project directory

   ```bash
   cd killer-sudoku-solver
   ```
   
## Usage
### Input Cage Configurations
- Provide the cage configurations in the specified format (sum,cell1,cell2,...), separated by semicolons. For example:
- 
   ```bash
   Enter cages (sum,cell1,cell2,...) separated by semicolon: 7,00,10;6,11,20,21;5,01,02;3,03,13;5,12,22;6,30,31;8,23,32,33
   ```
## Choose Solving Algorithm
- Select the solving algorithm by setting the algorithm variable in the code. Options are "BACKTRACKING" or "BACKJUMPING".

### Run the Program
- Execute the Python script to solve the puzzle:
   - Backjumping
   ```bash
   python sudokubackjump.py
   ```
   - Backtracking
   ```bash
   python sudokubacktrack.py
   ```
   - Simulated Annealing
   ```bash
   python SimAnnealling.py
   ```
## Examples
### Sample input for the program:
   ```bash
   7,00,10;6,11,20,21;5,01,02;3,03,13;5,12,22;6,30,31;8,23,32,33
   ```
### Output
  ```bash
   Solution found:
  2  4  1  3
  1  3  2  4
  4  1  3  2
  3  2  4  1
  Cages:
  Sum: 7, Cells: [(0, 0), (1, 0)]
  Sum: 6, Cells: [(1, 1), (2, 0), (2, 1)]
  Sum: 5, Cells: [(0, 1), (0, 2)]
  Sum: 3, Cells: [(0, 3), (1, 3)]
  Sum: 5, Cells: [(1, 2), (2, 2)]
  Sum: 6, Cells: [(3, 0), (3, 1)]
  Sum: 8, Cells: [(2, 3), (3, 2), (3, 3)]

   ```
## Dependencies
- Python 3.x

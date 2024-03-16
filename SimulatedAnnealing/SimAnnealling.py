# Killer Sudoku
# Paul Adrian O. Torres

import random
import math


# Fill a 4x4 grid with digits from 1 to 4.
# Each row and column must contain each digit exactly once.
# Each Cage must have the numbers within it sum up to the specified value.
# There should be no duplicated number within a cage.
# All cells must be covered by cages.

# SAMPLE INPUT FOR THE PROGRAM
#Sample 1
    # 4,00,10;3,01,02;7,03,13;9,11,20,21;6,12,22;5,30,31;6,23,32,33
#Sample 2
    # 7,00,10,20;5,01,02;6,03,12,13;5,11,21;7,30,31;4,22,32;6,23,33
#Sample 3
    # 7,00,10;6,11,20,21;5,01,02;3,03,13;5,12,22;6,30,31;8,23,32,33
    
    # SUM, Cell1, Cell2 .... = Cages
        # 7,00,10;
        # 6,11,20,21;
        # 5,01,02;
        # 3,03,13;
        # 5,12,22;
        # 6,30,31;
        # 8,23,32,33


class KillerSudoku:
    def __init__(self, size=4):
        self.size = size
        self.board = [[0 for _ in range(size)] for _ in range(size)]
        self.cages = []

    def parse_input(self, cage_str):
        parts = cage_str.split(',')
        sum_val = int(parts[0])
        cells = [(int(cell[0]), int(cell[1])) for cell in parts[1:]]
        self.cages.append((sum_val, cells))

    #Cages Sum and Cells input
    def get_input(self):
        print("Sample: 7,00,10,20;5,01,02;6,03,12,13;5,11,21;7,30,31;4,22,32;6,23,33")
        user_input = input("Enter cages (sum,cell1,cell2,...) separated by semicolon: ")
        cage_strs = user_input.split(';')
        
        for cage_str in cage_strs:
            self.parse_input(cage_str)

    #Check if cells has a duplicate and if all cells are covered
    def check_cells(self):
        covered_cells = set()
        
        for _, cells in self.cages:
            for cell in cells:
                if cell in covered_cells:
                    raise ValueError("Duplicate cell in cages")
                covered_cells.add(cell)
        if len(covered_cells) != self.size ** 2:
            raise ValueError("Not all cells are covered by cages")

    #Board
    def print_board(self):
        border = "+---" * self.size + "+"
        print("  0   1   2   3")
        print(border)
        for i in range(self.size):
            if i % int(math.sqrt(self.size)) == 0 and i != 0:
                print(border)
            for j in range(self.size):
                if j % int(math.sqrt(self.size)) == 0:
                    print("|", end=" ")
                print(f"{self.board[i][j]:2}", end=" ")
            print("|")
        print(border)
        print("Cages:")
        for sum_val, cells in self.cages:
            print(f"Sum: {sum_val}, Cells: {cells}")


    # Check if placing a number in a cell is valid
    def is_valid(self, row, col, num):
        if num in self.board[row]:
            return False
        if num in [self.board[i][col] for i in range(self.size)]:
            return False
        for cage_sum, cells in self.cages:
            if (row, col) in cells:
                cage_values = [self.board[r][c] for r, c in cells if self.board[r][c] != 0]
                if num in cage_values:
                    return False
                if len(cage_values) == len(cells) - 1 and sum(cage_values) + num != cage_sum:
                    return False
        return True

    # Find the first empty cell in the Sudoku board
    def find_empty_cell(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == 0:
                    return (i, j)
        return None

    #Solve the sudoku using Simulated Annealing Algorithm
    def solve(self):
        def cost(): #cost function to count empty cells
            cost = 0
            for i in range(self.size):
                for j in range(self.size):
                    if self.board[i][j] == 0:
                        cost += 1
            return cost

        def random_neighbor():
            i, j = random.randint(0, self.size - 1), random.randint(0, self.size - 1)
            return i, j, random.randint(1, self.size)

        def acceptance_probability(old_cost, new_cost, temperature):
            if new_cost < old_cost:
                return 1.0
            return math.exp((old_cost - new_cost) / temperature)

        #Variables
        current_cost = cost()
        T = 1.0
        T_min = 0.00001
        alpha = 0.9

        #Simulated Annealing Loop
        while True:  # Keep searching until a solution is found
            while T > T_min:
                i, j, num = random_neighbor()
                if self.is_valid(i, j, num):
                    old_cost = current_cost
                    old_num = self.board[i][j]
                    self.board[i][j] = num
                    current_cost = cost()
                    ap = acceptance_probability(old_cost, current_cost, T)
                    if random.random() > ap:
                        self.board[i][j] = old_num
                    else:
                        if current_cost == 0:
                            return True
                T *= alpha
            # If temperature drops below minimum and solution is not found, reinitialize and start again
            self.board = [[0 for _ in range(self.size)] for _ in range(self.size)]
            T = 1.0
            current_cost = cost()

if __name__ == "__main__":
    game = KillerSudoku()
    game.get_input()
    game.check_cells()

    if game.solve():
        print("Solution found:")
        game.print_board()
    else:
        print("No solution exists.")

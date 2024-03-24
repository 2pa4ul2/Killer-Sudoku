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

    def parse_cage_input(self, cage_str):
        parts = cage_str.split(',')
        sum = int(parts[0])
        cells = [(int(cell[0]), int(cell[1])) for cell in parts[1:]]
        self.cages.append((sum, cells))

    def get_cages_from_user(self):
        user_input = input("Enter cages (sum,cell1,cell2,...) separated by semicolon: ")
        cage_strs = user_input.split(';')
        for cage_str in cage_strs:
            self.parse_cage_input(cage_str)

    def check_cage_coverage(self):
        covered_cells = set()
        for _, cells in self.cages:
            for cell in cells:
                if cell in covered_cells:
                    raise ValueError("Duplicate cell in cages")
                covered_cells.add(cell)
        if len(covered_cells) != self.size ** 2:
            raise ValueError("Not all cells are covered by cages")

    def print_board(self):
        for row in self.board:
            print(' '.join(str(cell) for cell in row))
        print("Cages:")
        for sum, cells in self.cages:
            print(f"Sum: {sum}, Cells: {cells}")

    def is_valid(self, row, col, num):
        # Check row uniqueness
        if num in self.board[row]:
            return False
        # Check column uniqueness
        if num in [self.board[i][col] for i in range(self.size)]:
            return False
        # Check cage uniqueness
        for cage_sum, cells in self.cages:
            if (row, col) in cells:
                cage_values = [self.board[r][c] for r, c in cells if self.board[r][c] != 0]  # Exclude empty cells
                if num in cage_values:
                    return False
                if len(cage_values) == len(cells) - 1 and sum(cage_values) + num != cage_sum:
                    return False
        return True

    def solve(self, algorithm):
        empty_cell = self.find_empty_cell()
        if not empty_cell:
            return True  # Puzzle solved

        row, col = empty_cell
        for num in range(1, self.size + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if algorithm == "BACKTRACKING":
                    if self.solve(algorithm):
                        return True
                elif algorithm == "BACKJUMPING":
                    if self.solve_backjumping():
                        return True
                self.board[row][col] = 0  # Backtrack
        return False  # No solution found

    def solve_backjumping(self, last_conflict=None):
        empty_cell = self.find_empty_cell()
        if not empty_cell:
            return True

        row, col = empty_cell
        for num in range(1, self.size + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.solve_backjumping(last_conflict):
                    return True
                self.board[row][col] = 0

        if last_conflict:
            return False  # Backjumping occurred, no need to backtrack further
        return self.solve_backjumping((row, col))

    def find_empty_cell(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == 0:
                    return (i, j)
        return None


if __name__ == "__main__":
    game = KillerSudoku()
    game.get_cages_from_user()
    game.check_cage_coverage()

    # Set the algorithm to use (either "BACKTRACKING" or "BACKJUMPING")
    algorithm = "BACKJUMPING"

    if game.solve(algorithm):
        print("Solution found:")
        game.print_board()
    else:
        print("No solution exists.")

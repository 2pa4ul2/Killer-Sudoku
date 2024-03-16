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


    def solve(self):
        empty_cell = self.find_empty_cell()
        if not empty_cell:
            return True  # Puzzle solved

        row, col = empty_cell
        for num in range(1, self.size + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.solve():
                    return True
                self.board[row][col] = 0  # Backtrack
        return False  # No solution found

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

    if game.solve():
        print("Solution found:")
        game.print_board()
    else:
        print("No solution exists.")

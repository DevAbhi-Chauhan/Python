def print_grid(grid):
    for row in grid:
        print(" ".join(map(str, row)))

def is_valid_move(grid, row, col, num):
    # Check row and column for duplicates
    for i in range(9):
        if grid[row][i] == num or grid[i][col] == num:
            return False

    # Check 3x3 subgrid for duplicates
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if grid[i][j] == num:
                return False

    return True

def solve_sudoku(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                for num in range(1, 10):
                    if is_valid_move(grid, row, col, num):
                        grid[row][col] = num
                        if solve_sudoku(grid):
                            return True
                        grid[row][col] = 0  # Backtrack if the solution is not valid
                return False  # No valid move found, backtrack
    return True  # All cells filled, puzzle solved

# Example Sudoku puzzle (0 represents empty cells)
sudoku_grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

if solve_sudoku(sudoku_grid):
    print("Solved Sudoku:")
    print_grid(sudoku_grid)
else:
    print("No solution found.")


# 1.  print_grid is a helper function to print the Sudoku grid.
# 2. is_valid_move checks if a move (placing a number) is valid according to the Sudoku rules.
# 3. solve_sudoku is the main backtracking algorithm that attempts to fill in cells while checking for validity. 
# 4. It returns True if a solution is found and False otherwise.
# 5. You can input your Sudoku puzzle by modifying the sudoku_grid variable with the numbers you want to solve. 
# 6. This program should be able to solve Sudoku puzzles of varying difficulty levels as long as they have a valid solution.
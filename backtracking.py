# This class implements the N-Queens problem using backtracking
class NQueens_Backtracking:
    
    # Constructor method: initializes board size and sets up the board
    def __init__(self) -> None:
        self.size = int(input("Enter size of chessboard: "))  # User inputs N (size of NxN chessboard)
        # Initialize the chessboard with False values (no queens placed yet)
        self.board = [[False]*self.size for _ in range(self.size)]
        self.count = 0  # Counter to track number of valid solutions

    # Method to print the current state of the board
    def printBoard(self):
        for row in self.board:
            for ele in row:
                if ele == True:
                    print("Q", end=" ")  # 'Q' represents a queen
                else:
                    print(".", end=" ")  # '.' represents an empty cell
            print()
        print()  # Print newline between boards

    # Method to check if placing a queen at (row, col) is safe
    def isSafe(self, row: int, col: int) -> bool:
        
        # Check vertically in the current column for any queen
        for i in self.board:
            if i[col] == True:
                return False

        # Check backward slash (\) diagonal: top-left to bottom-right
        i = row
        j = col
        while i >= 0 and j >= 0:
            if self.board[i][j] == True:
                return False
            i -= 1
            j -= 1

        # Check forward slash (/) diagonal: top-right to bottom-left
        i = row
        j = col
        while i >= 0 and j < self.size:
            if self.board[i][j] == True:
                return False
            i -= 1
            j += 1

        # If all checks pass, position is safe
        return True

    # Recursive function to place queens row by row
    def solve(self, row: int):
        # Base case: All rows are filled successfully
        if row == self.size:
            self.count += 1  # Found a valid solution
            self.printBoard()  # Print the valid board configuration
            return

        # Try placing a queen in each column of the current row
        for col in range(self.size):
            if self.isSafe(row, col):  # Only proceed if it's safe
                self.board[row][col] = True  # Place the queen
                self.solve(row + 1)          # Recurse to next row
                self.board[row][col] = False  # Backtrack (remove queen)

# Create object of the class and start solving
solver = NQueens_Backtracking()
solver.solve(0)  # Start from row 0
print("Total number of solutions: ", solver.count)  # Print final solution count

#Time Complexity: O(N!) Space Complexity: O(N) or O(N^2), depending on implementation
#1, Optimization Approaches: Hill Climbing Assign one queen per column (so domain = row positions).Define a cost function: number of conflicts. Minimize this cost via stochastic or greedy strategies.
#Fast and scalable (works well for very large N, like N > 1000).
#2. Constraint Programming (CP): Model the N-Queens as a constraint satisfaction problem (CSP):Each variable is a queen.Each domain is the row positions.Constraints: No two queens in same row, column, or diagonal.

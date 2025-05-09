def branch():
    
    class NQueens_Branch_Bound_Stepwise:
        def __init__(self) -> None:
            # Input size of chessboard (N x N)
            self.size = int(input("Enter size of chessboard: "))  # Size of the chessboard (N x N)
            
            # Initialize the chessboard with all False values (No queens placed initially)
            self.board = [[False]*self.size for _ in range(self.size)]  # Initialize the board
            
            # Arrays to track if a column, forward diagonal or backward diagonal is occupied by a queen
            self.columns = [False] * self.size  # To track if a column is occupied
            self.fsDiagonal = [False] * (2 * self.size - 1)  # To track if forward diagonals are occupied
            self.bsDiagonal = [False] * (2 * self.size - 1)  # To track if backward diagonals are occupied
            
            # Count the number of solutions found
            self.count = 0  # To count the number of solutions

        def printBoard(self):
            """This function prints the chessboard with queens marked by 'Q' and empty spaces by '.'"""
            for row in self.board:
                # For each row, print 'Q' if the cell is True (queen placed), else print '.'
                print(" ".join("Q" if cell else "." for cell in row))
            print()  # Blank line after printing the board

        def isSafe(self, row, col):
            """
            Checks if it's safe to place a queen at position (row, col)
            This checks for conflicts in the same column or diagonals.
            """
            # Calculate diagonal indices for forward and backward diagonals
            fs = row + col  # Forward slash diagonal index
            bs = row - col + self.size - 1  # Backward slash diagonal index
            
            # If the column or any diagonal is already occupied, it's not safe to place a queen
            if self.columns[col] or self.fsDiagonal[fs] or self.bsDiagonal[bs]:
                # print(f"❌ Pruning at ({row}, {col}) — Column or Diagonal Conflict")
                return False  # Not safe
            return True  # Safe to place the queen

        def solve(self, row):
            """Recursively attempts to place queens on the board row by row."""
            
            # If we've placed queens on all rows, it's a valid solution
            if row == self.size:
                print("✅ Solution Found:")  # Solution found, print the board
                self.printBoard()  # Print the current arrangement of queens
                self.count += 1  # Increment the count of solutions found
                return

            # Try to place a queen in each column of the current row
            for col in range(self.size):
                #print(f"🔍 Trying to place Queen at ({row}, {col})...")

                if self.isSafe(row, col):  # If it's safe to place a queen in (row, col)
                    #print(f"✔️ Safe to place at ({row}, {col}) — placing Queen.")
                    
                    # Place the queen by marking the cell as True
                    self.board[row][col] = True
                    # Mark the column as occupied
                    self.columns[col] = True
                    
                    # Mark the forward and backward diagonals as occupied
                    fs = row + col
                    bs = row - col + self.size - 1
                    self.fsDiagonal[fs] = True
                    self.bsDiagonal[bs] = True

                    # Recurse to the next row to place the next queen
                    self.solve(row + 1)

                    # Backtrack: remove the queen from (row, col) and unmark the column and diagonals
                    #print(f"↩️ Backtracking from ({row}, {col}) — removing Queen.")
                    self.board[row][col] = False  # Remove the queen
                    self.columns[col] = False  # Unmark the column
                    self.fsDiagonal[fs] = False  # Unmark the forward diagonal
                    self.bsDiagonal[bs] = False  # Unmark the backward diagonal
                #else:
                    #print(f"❌ Not safe at ({row}, {col}) — trying next column.")

        def start(self):
            """Starts the N-Queens solver and tracks the time taken."""
            #start_time = time.time()  # Record the start time
            self.solve(0)  # Start solving from row 0
            # Print the total number of solutions and the time taken to find them
            print(f"\nTotal Solutions: {self.count}")
            #print(f"⏱️ Time Taken: {time.time() - start_time:.4f} seconds")

    # Run the NQueens solver with Branch and Bound method
    solver = NQueens_Branch_Bound_Stepwise()  # Create an instance of the solver class
    solver.start()  # Start the solution process
#branch()
def back():
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
#back()
def main():
    print("1. Branch and Bound")
    print("2. Backtracking")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        branch()
    elif choice == 2:
        back()
    else:
        print("Invalid choice!")
main()

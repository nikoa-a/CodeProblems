class ValidSudoku (object):

    def isValidSudoku(self, board):

        # Validate rows: Check each row for duplicate digits
        for row in board:
            # Set to store seen digits for the current row
            rowSet = set()
            for i in row:
                # If digit is already in the set, the row is invalid
                if i in rowSet:
                    return False
                # Ignore empty cells
                if i != ".":
                    rowSet.add(i) # Add the digit to the set

        # Validate columns: Check each column for duplicate digits
        for col in range(9):
            # Set to store seen digits for the current column
            colSet = set() 
            # Iterate through each row for the current column
            for j in range(9):
                # Access the cell in column `col` and row `j`
                item = board[j][col]
                # If digit is already in the set, the column is invalid
                if item in colSet:
                    return False
                # Ignore empty cells
                if item != ".":
                    colSet.add(item) # Add the digit to the set

        # Validate 3x3 boxes
        # Define starting points for all 3x3 boxes
        starts = [(0,0), (0,3), (0,6),
                  (3,0), (3,3), (3,6),
                  (6,0), (6,3), (6,6)]

        # For each 3x3 box starting point
        for i, j in starts:
            # Set to store seen digits for the current 3x3 box
            boxSet = set()
            # Iterate through the rows and columns within the 3x3 box
            for row in range(i, i+3):
                for col in range(j, j+3):
                    # Access the cell in the 3x3 box
                    item = board[row][col]
                    # If digit is already in the set, the box is invalid
                    if item in boxSet: 
                        return False
                    # Ignore empty cells
                    if item != ".":
                        boxSet.add(item) # Add the digit to the set
      
        # If no duplicates are found in rows, columns, and boxes, the board is valid
        return True

# Time complexity: O(n^2)
# Space complexity: O(n^2)
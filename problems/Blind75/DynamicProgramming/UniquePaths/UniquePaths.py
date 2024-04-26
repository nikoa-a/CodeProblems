class UniquePaths (object):

    def uniquePaths(self, m, n):

        # Initialize the first row with all 1s (represents the number of paths to reach each cell in the first row)
        # This row is the bottom row since we are starting from the bottom-right and going towars top-left
        paths = [1] * n

        # Iterate over each row (starting from the second row)
        for _ in range(m - 1):
            # Initialize a new row to store the number of paths for each cell in the current row
            new_paths = [1] * n

            # Update the number of paths for each cell in the current row based on the previous row
            for j in range(n - 2, -1, -1):
                # The number of paths to reach the current cell is the sum of paths from the cell to its right and the cell above it
                new_paths[j] = new_paths[j + 1] + paths[j]

            # Update the current row with the calculated number of paths
            paths = new_paths

        # Return the number of paths to reach the bottom-right cell (top-left cell has index [0, 0])
        return paths[0]

import collections

class NumberOfIslands (object):

    def numIslands(self, grid):

        # Base case: return 0 if the grid is empty
        if not grid:
            return 0
        
        # Initialize the number of rows and columns in the grid
        rows, cols = len(grid), len(grid[0])
        # Initialize a set to keep track of visited cells
        visited = set()
        # Initialize a variable to keep track of the number of islands
        island_count = 0

        # Define a helper function to perform a breadth-first search
        def bfs(start_row, start_col):
            # Initialize a queue to keep track of cells to visit
            queue = collections.deque()
            # Mark the starting cell as visited
            visited.add((start_row, start_col))
            # Add the starting cell to the queue
            queue.append((start_row, start_col))

            # Iterate until the queue is empty
            while queue:
                # Get the current cell from the queue
                row, col = queue.popleft()
                # Define the four directions to move in the grid
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                # Explore neighboring cells in each direction
                for d_row, d_col in directions:
                    # Calculate the coordinates of the neighboring cell
                    new_row, new_col = row + d_row, col + d_col
                    # Check if the new cell is within the grid boundaries and is unvisited
                    if (0 <= new_row < rows and
                        0 <= new_col < cols and
                        grid[new_row][new_col] == "1" and
                        (new_row, new_col) not in visited):
                        # Add the new cell to the queue for further exploration
                        queue.append((new_row, new_col))
                        # Mark the new cell as visited
                        visited.add((new_row, new_col))
                            
        # Iterate over each cell in the grid
        for row in range(rows):
            for col in range(cols):
                # Check if the current cell represents land and is unvisited
                if grid[row][col] == "1" and (row, col) not in visited:
                    # Perform breadth-first search starting from the current cell
                    bfs(row, col)
                    # Increment the number of islands
                    island_count += 1

        # Return the total number of islands
        return island_count

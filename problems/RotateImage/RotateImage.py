class RotateImage (object):

    def rotate(self, matrix):

        # Initialize the left pointer to index 0
        left = 0
        # Initialize the right pointer to the last index of the matrix
        right = len(matrix) - 1

        # Iterate while the left pointer is less than the right pointer
        while left < right:
            # Iterate through the current layer
            for i in range(right - left):
                # Initialize the top and bottom pointers, 'i' variable is the offset
                top = left
                bottom = right

                # Store the top-left value in a temporary variable
                topLeft = matrix[top][left + i]

                # Move bottom-left value to top-left
                matrix[top][left + i] = matrix[bottom - i][left]

                # Move bottom-right value to bottom-left
                matrix[bottom - i][left] = matrix[bottom][right - i]

                # Move top-right value to bottom-right
                matrix[bottom][right - i] = matrix[top + i][right]

                # Move top-left (stored in temp) to top-right
                matrix[top + i][right] = topLeft

            # Move the pointers inwards for the next layer
            left += 1
            right -= 1     

        return

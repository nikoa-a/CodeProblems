class ContainerWithMostWater (object):

    def maxArea(self, height):

        # Initialize two pointers to the beginning and end of the list
        left = 0
        right = len(height) - 1
        # Initialize the variable to store the maximum water
        water = 0

        # Loop through the list until the two pointers meet
        while left < right:

            # Calculate the area of the container
            # The area is the width of the container (right - left) times the height of the container (the minimum of the two heights)
            newWater = (right - left) * min(height[left], height[right])

            # Update the maximum water if the new water is greater
            water = max(water, newWater)

            # Move the pointer with the smaller height towards the center
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        # Return the maximum water
        return water

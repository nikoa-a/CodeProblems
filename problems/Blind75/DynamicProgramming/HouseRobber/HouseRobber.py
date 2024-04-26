class HouseRobber (object):

    def rob(self, nums):

        # Initialize the variables to store the previous and current maximum values
        rob1 = 0
        rob2 = 0

        # Note: We can't rob two adjacent houses, so we can't rob rob2 and num at the same time
        # [rob1, rob2, num, num+1, ...]
        
        # Iterate through the list of numbers
        for num in nums:
            # Store the current maximum value in a temporary variable
            temp = max(num + rob1, rob2)
            # Update the previous and current maximum values
            rob1 = rob2
            rob2 = temp

        # Return the current maximum value
        return rob2

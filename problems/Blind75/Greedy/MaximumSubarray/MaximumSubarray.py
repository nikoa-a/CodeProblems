class MaximumSubarray (object):

    def maxSubarray(self, nums):

        # Initialize the maximum subarray sum with the first element
        maxSubArray = nums[0]
        # Initialize the current sum to 0
        currentSum = 0

        # Iterate through the array
        for n in nums:
            # If the current sum becomes negative, reset it to 0
            if currentSum < 0:
                currentSum = 0

            # Add the current number to the current sum to extend the subarray
            currentSum += n
            
            # Update the maximum subarray sum if the current sum is greater
            maxSubArray = max(maxSubArray, currentSum)

        # Return the maxSubArray
        return maxSubArray

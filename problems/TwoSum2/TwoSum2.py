class TwoSum2 (object):

    def twoSum(self, nums, target):

        # Initialize two pointers to the start and end of the list
        left = 0
        right = len(nums) - 1

        # Iterate through the list until the pointers meet
        while left < right:
            # Calculate the sum of the elements at the pointers
            currentSum = nums[left] + nums[right]

            # If the sum is greater than the target, move the right pointer to the left
            if currentSum > target:
                right -= 1
            # If the sum is less than the target, move the left pointer to the right
            elif currentSum < target:
                left += 1
            # If the sum is equal to the target, return the indexes of the elements
            else:
                return [left + 1, right + 1]
            
        # Return an empty list if no solution is found
        return []

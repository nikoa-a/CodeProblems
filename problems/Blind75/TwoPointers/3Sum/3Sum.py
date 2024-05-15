class ThreeSum (object):

    def threeSum(self, nums):
        
        # Sort the list for easier comparison
        nums.sort()
        # Initialize an empty list to store the results
        res = []

        # Iterate through the list of numbers
        for i, num in enumerate(nums):
            # Skip duplicates to avoid duplicate results
            if i > 0 and num == nums[i - 1]:
                continue

            # Initialize two pointers to the start and end of the list
            left = i + 1
            right = len(nums) - 1
            # Iterate through the list until the pointers meet
            while left < right:
                # Calculate the sum of the elements at the pointers
                currentSum = num + nums[left] + nums[right]
                # If the sum is greater than 0, move the right pointer to the left
                if currentSum > 0:
                    right -= 1
                # If the sum is less than 0, move the left pointer to the right
                elif currentSum < 0:
                    left += 1
                # If the sum is equal to 0, add the elements to the result list and move the left pointer
                else:
                    res.append([num, nums[left], nums[right]])
                    left += 1
                    # Skip duplicates to avoid duplicate results
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        # Return the result list            
        return res

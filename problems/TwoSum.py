class twoSum (object):

    def twoSum(self, nums, target):
        
        # Create a dictionary to store elements and their indexes
        numMap = {}

        # Iterate through the list of numbers
        for i, num in enumerate(nums):
            # Calculate the complement of the current number
            complement = target - num
            # Check if the complement exists in the dictionary
            if complement in numMap:
                # Retrun the indexes of the current element and its complement
                return [numMap[complement], i]
            
            # Add the current element to the dictionary
            numMap[num] = i

        # If no solution is found
        return

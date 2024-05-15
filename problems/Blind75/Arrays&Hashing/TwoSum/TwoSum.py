class TwoSum (object):

    def twoSum(self, nums, target):
        
        numMap = {} # Create a dictionary to store elements and their indexes

        for i, num in enumerate(nums): # Iterate through the list of numbers
            complement = target - num # Calculate the complement of the current number
            if complement in numMap: # Check if the complement exists in the dictionary
                return [numMap[complement], i] # Retrun the indexes of the current element and its complement
            
            numMap[num] = i # Add the current element to the dictionary

        return # Return None if no solution is found

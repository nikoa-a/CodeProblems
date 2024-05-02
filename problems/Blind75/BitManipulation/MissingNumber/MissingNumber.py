class MissingNumber (object):

    def missingNumber(self, nums):

        # Initialize missing number as the last number in the sequence
        missing = len(nums)
    
        # Iterate through the list of numbers
        for i, num in enumerate(nums):
            # XOR the index and the number with the current missing number
            # This effectively cancels out the existing numbers in nums, leaving the missing number
            missing ^= i ^ num

        # Return the missing number   
        return missing

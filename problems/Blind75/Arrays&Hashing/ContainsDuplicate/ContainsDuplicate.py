class ContainsDuplicate (object):

    def containsDuplicate(self, nums):
            
        # Create a set to store the numbers    
        numSet = set()

        # Iterate through the numbers
        for n in nums:
            # If the number is already in the set, return True
            if n in numSet:
                return True
            
            # Otherwise, add the number to the set
            numSet.add(n)

        # If no duplicates are found, return False
        return False

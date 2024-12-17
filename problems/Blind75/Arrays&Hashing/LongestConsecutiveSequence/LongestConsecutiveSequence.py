class LongestConsecutiveSequence (object):

    def longestConsecutive(self, nums):

        # Convert the nums list into a set for O(1) lookups
        numsSet = set(nums)
        # Initialize variable to keep track of the longest consecutive sequence
        longest = 0

        # Iterate through each number in the set
        for n in numsSet:
            # If the number does not have a left neighbor, it's the start of a sequence
            if (n - 1) not in numsSet:
                current = 0 # Initialize the current sequence length to 0

                # Check for consecutive numbers by looking for right neighbors
                while (n + current) in numsSet:
                    current += 1

                # Update the longest sequence length if the current sequence is longer
                longest = max(current, longest)

        # Return the length of the longest consecutive sequence
        return longest

# Time complexity: O(n)
# Space complexity: O(n)
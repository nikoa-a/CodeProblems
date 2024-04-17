class LongestSubstringWORepeatingChar (object):

    def lengthOfLongestSubstring(self, s):

        # Initialize a set to store the unique characters seen so far
        uniqueLetters = set()
        # Initialize the length of the current longest substring without repeating characters
        currentLongest = 0
        # Initialize the left pointer which represents the start of the current substring
        left = 0

        # Iterate through the string with the right pointer
        for right in range(len(s)):
            # Check if the character at the right pointer is already in the set of unique characters
            while s[right] in uniqueLetters:
                # Remove the character at the left pointer
                uniqueLetters.remove(s[left])
                # Move the left pointer to the right
                left += 1

            # Add the character at the right pointer to the set of unique characters
            uniqueLetters.add(s[right])
            # Update the length of the longest substring if necessary
            currentLongest = max(currentLongest, right - left + 1)

        # Return the longest substring
        return currentLongest

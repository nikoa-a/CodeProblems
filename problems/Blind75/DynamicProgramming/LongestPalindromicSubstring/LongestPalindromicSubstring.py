class LongestPalindromicSubstring (object):

    def longestPalindrome(self, s):

        # Initialize the result string and its length
        result = ""
        resultLen = 0

        # Iterate through the string
        for i in range(len(s)):
            # Call the helper function to expand from the center for odd length palindromes
            result, resultLen = self.expandFromCenter(s, i, i, result, resultLen)
            # Call the helper function to expand from the center for even length palindromes
            result, resultLen = self.expandFromCenter(s, i, i + 1, result, resultLen)

        # Return the result
        return result
    
    # Helper function to expand from the center
    def expandFromCenter(self, s, left, right, result, resultLen):
        # While the left and right pointers are within the bounds of the string and the characters are equal
        while left >= 0 and right < len(s) and s[left] == s[right]:
            # If the length of the palindrome is greater than the current result length
            if (right - left + 1) > resultLen:
                # Update the result and the result length
                result = s[left:right + 1]
                resultLen = right - left + 1
            # Move the left pointer to the left and the right pointer to the right
            left -= 1
            right += 1
        # Return the result and the result length
        return result, resultLen

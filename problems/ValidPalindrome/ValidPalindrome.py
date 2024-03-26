class ValidPalindrome (object):

    def isPalindrome(self, s):

        # Initialize two pointers to the beginning and end of the string
        left = 0
        right = len(s) - 1

        # Loop through the string until the two pointers meet
        while left < right:
            # Skip non-alphanumeric characters
            while left < right and not s[left].isalnum():
                # Move the left pointer to the right
                left += 1
            # Skip non-alphanumeric characters
            while right > left and not s[right].isalnum():
                # Move the right pointer to the left
                right -= 1

            # Compare the characters at the left and right pointers
            if s[left].lower() != s[right].lower():
                # If the characters are not equal, return False
                return False
            
            # Move the pointers towards the center
            left += 1
            right -= 1

        # If the loop completes, return True
        return True

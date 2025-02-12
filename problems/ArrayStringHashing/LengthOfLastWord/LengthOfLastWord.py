class LengthOfLastWord:

    def lengthOfLastWord(self, s):

        length = 0

        for char in s[::-1]: # Iterate backwards
            if char != " ": # Find the first non-space character
                length += 1 # Increment the length
            elif char == " " and length > 0: # Find first empty space when the length is over 0
                return length # Return the length
            
        return length # Otherwise return length here, "0" in this case
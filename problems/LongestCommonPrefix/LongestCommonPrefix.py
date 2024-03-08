class LongestCommonPrefix:

    def longestCommonPrefix (self, strs):

        # If the list is empty, return an empty string
        if len(strs) == 0:
            return ""
        
        # Take the first word from the list
        firstWord = strs[0]
        
        # Outer loop: Iterate through each letter of the first word in the list, 'firstWord'
        for i in range(len(firstWord)):
            # Inner-loop. We iterate through the rest of the words in the list, starting from the second one "strs[1:]"
            for word in strs[1:]:
                # Check if the 'firstWord' is longer than the current word or if the letters don't match 
                if i == len(word) or word[i] != firstWord [i]:
                    # Return the 'firstWord' from the first letter to the current index
                    return firstWord[0:i]
                
        # If the first word is the shortest, we move out of the outer-loop and return the 'firstWord'  
        return firstWord

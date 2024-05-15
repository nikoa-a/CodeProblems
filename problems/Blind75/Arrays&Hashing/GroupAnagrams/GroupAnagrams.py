class GroupAnagrams (object):

    def groupAnagrams(self, strs):

        # Initialize an empty dictionary to store the anagram groups
        result = {}

        # Iterate through the list of strings
        for s in strs:
            # Create a list of 26 zeros to store the frequency of each character in the string (a ... z)
            count = [0] * 26

            # Iterate through the characters of the string
            for c in s:
                # Increment the frequency of the character in the list 
                count[ord(c) - ord("a")] += 1  # ASCII Value of c minus ASCII value of 'a'

            # Convert the list of character counts to a tuple to use it as a key
            key = tuple(count)

            # Add the word to the list of anagrams for the corresponding key
            if key in result:
                result[key].append(s)
            else:
                result[key] = [s]

        # Return the values of the dictionary, which are the grouped anagrams
        return result.values()

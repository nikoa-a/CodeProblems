class ValidAnagram (object):

    def isAnagram(self, s, t):

        # If the length of the strings are different, they can't be anagrams
        if len(s) != len(t):
            return False
        
        # Create two dictionaries to store the frequency of each character in the strings
        s_freq = {}
        t_freq = {}

        # Iterate trough the characters of the first string
        for char in s:
            # If the character is not in the dictionary, add it with a frequency of 1, otherwise increment the frequency by 1
            s_freq[char] = s_freq.get(char, 0) + 1

        # Iterate trough the characters of the second string
        for char in t:
            # If the character is not in the dictionary, add it with a frequency of 1, otherwise increment the frequency by 1
            t_freq[char] = t_freq.get(char, 0) + 1

        # If the dictionaries are equal, the strings are anagrams
        return s_freq == t_freq


# Time complexity: O(n + m)
# Space complexity: O(1) since we have at most 26 different characters
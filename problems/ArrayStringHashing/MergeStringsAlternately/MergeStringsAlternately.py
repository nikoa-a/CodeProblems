class MergeStringsAlternately:

    def mergeAlternately(self, word1, word2):

        merged = []
        w1Pointer, w2Pointer = 0, 0

        while w1Pointer < len(word1) and w2Pointer < len(word2):
            merged.append(word1[w1Pointer])
            merged.append(word2[w2Pointer])
            w1Pointer += 1
            w2Pointer += 1

        # Append the remaining characters starting from pointer.
        # If pointer is out of bounds, nothing will be added
        merged.append(word1[w1Pointer:])
        merged.append(word2[w2Pointer:])

        return "".join(merged)
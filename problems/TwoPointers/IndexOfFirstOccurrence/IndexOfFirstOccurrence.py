class IndexOfFirstOccurrence:

    def strStr(self, haystack, needle):

        if not needle:
            return 0

        hPointer, nPointer = 0, 0 # Haystack and needle pointers
        first = -1 # Track where the first match starts

        while hPointer < (len(haystack)):
            if haystack[hPointer] == needle[nPointer]:
                if nPointer == 0:
                    first = hPointer  # Set first occurrence index
                if nPointer == len(needle) - 1:
                    return first  # Found the full match
                nPointer += 1  # Move needle pointer

            else:
                if nPointer > 0:
                    hPointer = first # Reset haystack pointer to recheck (prevents skipping valid matches)
                nPointer = 0 # Reset needle pointer
                first = -1 # Reset first index

            hPointer += 1 # Move haystack pointer

        return -1
class NumberOf1Bits (object):

    def hammingWeight(self, n):

        # Initialize a counter to store the number of set (1) bits
        ones = 0

        # Iterate through the bits of the number
        while n:
            # If the last bit is 1, increment the counter
            ones += n % 2
            # Shift the bits to the right to process the next bit
            n = n >> 1

        # Return the total count of set bits
        return ones

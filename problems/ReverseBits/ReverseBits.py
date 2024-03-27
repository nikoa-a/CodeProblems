class ReverseBits (object):

    def reverseBits(self, n):
        # Initialize the result to 0 to store the reversed bits
        res = 0
        # Process all the bits in n
        for _ in range(32):
            # Extract the rightmost bit of n and append it to the result
            res = (res << 1) | (n & 1)
            # Shift n to the right by 1 to process the next bit
            n >>= 1
        # Return the result
        return res

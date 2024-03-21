class CountingBits (object):

    def countBits(self, n):

        # Initialize an array to store the number of set (1) bits for each number from 0 to n
        ans = [0] * (n +1)

        # Iterate through the numbers from 1 to n 
        for i in range(1, n + 1):
            # Count the set bits for the right-shifted counterpart of i
            # and add the count of the least significant bit of i
            ans[i] = ans[i >> 1] + (i & 1)

        # Return the array of set bits
        return ans

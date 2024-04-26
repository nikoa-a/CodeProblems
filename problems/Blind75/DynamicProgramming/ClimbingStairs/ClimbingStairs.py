class ClimbingStairs (object):

    # This is just a simple Fibonacci sequence problem
    def climbStairs(self, n):

        # Base case variables
        n1 = 0
        n2 = 1
        i = 0

        # Loop through the sequence until we reach the nth number
        while i < n:
            # Calculate the next number in the sequence
            sum = n1 + n2
            # Set the next number in the sequence to the temporary variable
            n1 = n2
            # Set the sum to the next number in the sequence
            n2 = sum
            # Increment the counter
            i += 1

        # Return the sum
        return sum

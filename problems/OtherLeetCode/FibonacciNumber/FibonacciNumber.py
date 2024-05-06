class FibonacciNumber (object):

    def fibonacciNumber(self, n):

        # Base case variables
        sum = 0
        n2 = 1
        i = 0

        # Loop through the sequence until we reach the nth number
        while i < n:
            # Calculate the next number in the sequence
            temp = sum + n2
            # Set the sum to the next number in the sequence
            sum = n2
            # Set the next number in the sequence to the temporary variable
            n2 = temp
            # Increment the counter
            i += 1

        # Return the sum
        return sum

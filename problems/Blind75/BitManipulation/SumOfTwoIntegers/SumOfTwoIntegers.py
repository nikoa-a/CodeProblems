class SumOfTwoIntegers (object):

    def getSum(self, a, b):

        # Define a recursive function to perform addition without using the '+' operator
        def add(a, b):
            # If either 'a' or 'b' is 0, return the non-zero value
            if not a or not b:
                return a or b
            # Recursively add the sum of the bitwise XOR and the carry shifted to the left by 1
            return add(a ^ b, (a & b) << 1)

        # If both 'a' and 'b' have different signs
        if a * b < 0: 
            # Swap 'a' and 'b' if 'a' is positive
            if a > 0:
                return self.getSum(b, a)
            # Check for overflow or underflow conditions
            if add(~a, 1) == b:
                return 0
            if add(~a, 1) < b:  
                return add(~add(add(~a, 1), add(~b, 1)), 1) 
            
        # Return the sum using the defined add function
        return add(a, b)

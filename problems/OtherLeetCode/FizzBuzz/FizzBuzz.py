class FizzBuzz (object):

    def fizzBuzz(self, n):

        # Create an empty list to store the output
        output = []

        # Iterate through the range of 1 to n
        for i in range(1, n + 1):
            # Check if the current number is divisible by 3 and 5
            if i % 3 == 0 and i % 5 == 0:
                output.append("FizzBuzz")
            # Check if the current number is divisible by 3
            elif i % 3 == 0:
                output.append("Fizz")
            # Check if the current number is divisible by 5
            elif i % 5 == 0:
                output.append("Buzz")
            # If none of the above conditions are met, append the number as a string
            else:
                output.append(str(i))
        
        # Return the list
        return output

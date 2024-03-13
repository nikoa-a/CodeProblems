class PrintStaircase (object):

    def printStaircase(n):

        # Outer-loop. Loop through the range of n
        for i in range(n):
            output = ["-"] * n  # Create a list of n dashes
            for j in range(i + 1): # Inner-loop. Loop through the range of i + 1
                output[n - j - 1] = "#"  # Replace dashes with "#" from the end
            print("".join(output)) # Print the output

        return


# Test case 1
instance = PrintStaircase
instance.printStaircase(5)

# Test case 2
instance = PrintStaircase
instance.printStaircase(3)

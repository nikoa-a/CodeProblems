class RomanToInteger (object):

    def romanToInt (self, s):

        # Create a dictionary to store the roman numerals and their corresponding values
        romanNumbers = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D":500, "M": 1000}

        # List to store the splitted string
        List = [*s]

        # Variables to store the number and the last number
        number = 0
        last = 0

        # Loop through the 'List'
        for x in List:    
            # If the last number is less than the current number 
            if last < romanNumbers[x]:
                # Subtract the last number from the final number
                number = number - last
                # Add the current number minus the last number to the final number
                number = number + romanNumbers[x] - last
            # Else, add the current number to the final number
            else:
                number = number + romanNumbers[x]

            # Update the last number
            last = romanNumbers[x]
            
        # Return the final number    
        return number

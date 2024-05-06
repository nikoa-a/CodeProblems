class PalindromeNumber (object):

    def isPalindrome(self, x):

        # If the number is negative or ends with 0, it cannot be a palindrome
        if x < 0 or (x != 0 and x % 10 == 0): 
            return False

        half = 0 # variable to store the reversed half of the 'x'
        while x > half: # loop while the first half 'x' is greater than the second half 'half'
            half = (half * 10) + (x % 10) # get the last digit of the 'x' and add it to the 'half'
            x = x // 10 # remove the last digit from the 'x'

        # if the number of digits is odd, we need to remove the last digit from the 'half'
        return x == half or x == half // 10
    
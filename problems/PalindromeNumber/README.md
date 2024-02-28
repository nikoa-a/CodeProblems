## Palindrome Number

Given an integer x, return true if x is a palindrome, and false otherwise.

Challenge is to solve it without converting the integer to a string.

Solving this with converting the integer to a string would look like this:

```python
def isPalindrome(self, x):

    # Convert the number to a string and compare it to its reverse and return the result
    return str(x) == str(x)[::-1]
```
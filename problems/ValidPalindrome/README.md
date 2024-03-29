## Valid Palindrome

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

---

#### Example 1:
> **Input:** s = "A man, a plan, a canal: Panama"<br>
> **Output:** true<br>
> **Explanation:** "amanaplanacanalpanama" is a palindrome.

#### Example 2:
> **Input:** s = "race a car"<br>
> **Output:** false<br>
> **Explanation:** "raceacar" is not a palindrome.

Easiest solution to this problem that creates new string:

```python
def isPalindrome(self, s):

        newString = ""
        for c in s:
            if c.isalnum():
                newString += c.lower()

        return newString == newString[::-1]
```

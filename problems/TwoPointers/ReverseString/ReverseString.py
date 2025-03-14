class ReverseString:

    def reverseString(self, s):

        left, right = 0, len(s) - 1

        while left <= right:
            temp = s[left]
            s[left] = s[right]
            s[right] = temp
            left += 1
            right -= 1

        return s
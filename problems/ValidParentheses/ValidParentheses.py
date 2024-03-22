class ValidParentheses (object):

    def isValid(self, s):

        # Map of closing brackets to their corresponding opening brackets
        bracketMap = {')': '(', '}': '{', ']': '['}  
        # Stack to keep track of opening brackets
        stack = []

        # Iterate through each character in the string
        for char in s:
            # If the character is an opening bracket, push it onto the stack
            if char in bracketMap.values():
                stack.append(char)
            # If the character is a closing bracket
            elif char in bracketMap:
                # Check if the stack is not empty and if the top of the stack matches the corresponding opening bracket
                if stack and stack[-1] == bracketMap[char]:
                    # Pop the corresponding opening bracket from the stack
                    stack.pop()
                # If the stack is empty or if the top of the stack doesn't match the corresponding opening bracket
                else:
                    # The string is invalid, so return False
                    return False

        # After iterating through the entire string, if the stack is empty, the string is valid
        if len(stack) == 0:
            return True
        
        # If the stack is not empty, there are unmatched opening brackets, so the string is invalid
        return False

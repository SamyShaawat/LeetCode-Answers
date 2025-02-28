class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }
        stack = []
        for char in s:
            # If the character is not a closing bracket (i.e., it's an opening bracket),
            # then add it to the stack.
            if char not in hashmap:
                stack.append(char)
            else:
                # If the character is a closing bracket, first check if the stack is empty.
                # An empty stack means there's no matching opening bracket.
                if not stack:
                    return False
                # Pop the last opening bracket from the stack.
                else:
                    popped = stack.pop()
                    # Compare the popped opening bracket with the expected one for the current closing bracket.
                    # If they don't match, the string is not valid.
                    if popped != hashmap[char]:
                        return False
        # After processing all characters, check if the stack is empty.
        # A non-empty stack indicates there are unmatched opening brackets.
        # Return True if the stack is empty (all brackets matched correctly), otherwise False.
        return not stack
        
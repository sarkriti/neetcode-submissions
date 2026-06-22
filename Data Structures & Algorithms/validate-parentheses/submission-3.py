class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {")":"(", "]" : "[", "}":"{"}

        for char in s:
            if char in closeToOpen: #c is the close parenthesis
                if stack and stack[-1] == closeToOpen[char]: #checks to see if top element is the open parenthesis
                    stack.pop()
                else: #we have a close parenthesis with no corresponding open
                    return False
            else:
                stack.append(char) #we are adding the char to the stack
        return not stack

                

        
class Solution:
    def isValid(self, s: str) -> bool:
        """
        Use a stack: if it is an opening symbol, insert in the stack.
        If it is a closing one, pop from the stack and check whether it
        is of the same 'type'
        """
        symbols = {
            ')':'(',
            ']':'[',
            '}':'{'
        }
        my_stack = []

        for c in s:
            if c in ('(','[','{'):
                my_stack.append(c)
            else:
                if not my_stack:
                    return False
                if my_stack.pop() != symbols[c]:
                    return False
        
        return len(my_stack) == 0
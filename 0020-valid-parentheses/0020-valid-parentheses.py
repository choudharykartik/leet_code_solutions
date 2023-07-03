class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {'(':')','{':'}','[':']'}
        stack = []
        for char in s:
            if char in mapping or not stack:
                stack.append(char)
            else:
                stack_value = stack[-1]
                if mapping.get(stack_value) and  mapping[stack_value] ==char:
                    stack.pop()
                else:
                    return False
        
        return not stack
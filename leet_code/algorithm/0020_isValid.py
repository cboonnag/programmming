class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        if len(s)%2 == 1:
            return False
        
        for c in s: 
            if c in ['(','[','{']:
                stack.append(c)
            elif (len(stack) > 0):
                prev_c = stack.pop()
                if prev_c == "(" and c != ")":
                    return False
                elif prev_c == "[" and c != "]":
                    return False
                elif prev_c == "{" and c != "}":
                    return False
            else:
                return False
            
        return len(stack) == 0
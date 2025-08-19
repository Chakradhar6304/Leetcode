class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 == 1:
            return False
        
        stack = []
        match = {')': '(', ']': '[', '}': '{'}
        
        for ch in s:
            if ch in match.values():          
                stack.append(ch)
            else:                             
                if not stack or stack[-1] != match.get(ch):
                    return False
                stack.pop()
        
        return not stack
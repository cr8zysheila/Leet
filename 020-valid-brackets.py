class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pairs = {')': '(', ']':'[', '}':'{'}
        stack = []
        for c in s:
            if c in pairs.values():
                stack.append(c)
            elif c in pairs.keys():
                print c, pairs[c]
                if stack and stack[-1] == pairs[c]:
                    stack.pop()
                else:
                    return False

        return not stack

print Solution().isValid("()")
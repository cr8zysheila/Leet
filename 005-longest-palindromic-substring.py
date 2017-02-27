class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        b, e = 0, 0
        for i in range(0, len(s)-1):
            for j in range(0, 2):
                l, h = self.palindrome(s, i, i+j)
                if h - l > e - b:
                    b, e = l, h

        return s[b:e+1]

    def palindrome(self, s, c1, c2):
        if s[c1] != s[c2]:
            return c1, c1
        while c1 >= 0 and c2 < len(s):
            if s[c1] == s[c2]:
                c1, c2 = c1 - 1, c2 + 1
            else:
                break

        return c1 + 1, c2 - 1

print Solution().longestPalindrome("babad")
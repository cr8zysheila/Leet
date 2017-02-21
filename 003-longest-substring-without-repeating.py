class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        """use this line  for leetcode oj
        if type(s) is not unicode or s == "":
        """

        if type(s) is not str or s == "":
            return 0

        appeared = {}
        l, h, cl, ch = 0, 0, 0, 0
        appeared[s[0]] = 0
        for i, c in enumerate(s[1:]):
        	if c in appeared and cl <= appeared[c] <= ch:
        		cl = appeared[c] + 1
        	
        	appeared[c] = i + 1
        	ch = i + 1

        	if ch - cl > h - l:
        		h = ch
        		l = cl

        print s[l:h+1]
        return h - l + 1


Solution().lengthOfLongestSubstring("abcdc")
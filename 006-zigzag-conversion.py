''' solution 1
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows <= 1:
        	return s

        strLists = []
        strings = []
        for i in range(0, numRows):
        	strLists.append([])

        self.convertToStrList(s, numRows, strLists)

        for i in range(0, numRows):
        	row = "".join(strLists[i])
        	strings.append(row)

        result = "".join(strings)

        return result

    def convertToStrList(self, s, numRows, strLists):
    	r = 0
    	step = -1
    	for c in s:
    		strLists[r].append(c)
    		if r == numRows - 1 or r == 0:
    			step = step * (-1)
    		r += step
'''

'''solution 2: performance is worse than solution1'''
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        strList = []
        """steps for each row to find the next character in s. For the first and 
        the last row, it's 2*(numRows - 1). For the rows in the middle, the step
        alternates between 2*(numrows - 1) - row*2 and row*2
        """
        steps = []
      
        for row in range(0, numRows - 1):
        	steps.append(2 * (numRows - 1) - row * 2)
        # add the step for the last row
        steps.append(2 * (numRows - 1))

        for row in range(0, numRows):
        	i = row
        	while i < len(s):
        		strList.append(s[i])
        		i += steps[row]
        		nextStep = 2 * (numRows - 1) - steps[row]
        		if nextStep > 0:
        			steps[row] = nextStep


        return "".join(strList)

print Solution().convert("PAYPALISHIRING", 3)


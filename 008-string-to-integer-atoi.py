class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        INT_MAX =  2147483647
        INT_MIN = -2147483648
        digits = '0123456789'
        num = 0
        inNumber = False
        sign = 0
        for c in str:
        	if inNumber == False:
        		if c == " ":
        			continue
        		
        		elif c == "-" and sign == 0:
        			sign = -1
        			inNumber = True
        		elif c == "+" and sign == 0:
        			sign = 1
        			inNumber = True
        		elif c in digits:
        			num = num * 10 + ord(c) - ord('0')
        			inNumber = True
        			if sign == 0:
        				sign = 1
        		else:
        			break
        	elif c in digits:
        		d = ord(c) - ord('0')
        		limit = INT_MAX - d if sign > 0 else INT_MIN + d
        		if num <= INT_MAX//10 and num * 10 < sign * limit:
        			num = num * 10 + d
        		else:
        			if sign == 1: 
        				return INT_MAX
        			if sign == -1: 
        				return INT_MIN

        	else:
        		break

        return sign * num

print Solution().myAtoi("2147483649")
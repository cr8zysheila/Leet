'''solution 1
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
        	return -self.reverse(-x)

        result = 0
        while x >= 10:
        	result = result * 10 + x % 10
        	x = x // 10

        print result
        print 0x7FFFFFFF
        if result <= 0x7FFFFFFF//10:
        	return result*10 + x

        # overflow
        else:
        	return 0
'''
''' solution 2: slower than solution 1'''
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
        	return -self.reverse(-x)

        max_int_str = str(0x7FFFFFFF)
        x_rev_str = str(x)[::-1]
        print max_int_str, x_rev_str
        if len(x_rev_str) == len(max_int_str) and x_rev_str > max_int_str:
        	return 0
        return int(x_rev_str)

print Solution().reverse(-2147483412)
print Solution().reverse(123)

#2147483647
#2143847412
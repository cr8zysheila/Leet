# write code for leetcode water container problem and trapping water problem



class TreeNode(object):
	def __init__(self, value):
		self.left = None
		self.right = None
		self.val = value


# this solution is for 'super balanced tree' defined in the IC 
# problem, which has a different definition for 'balanced' in leetcode 110.
# In leetcode 110, the definition for balenced is the same as in an AVL
# tree. In an AVL tree, the difference between the depths of two subtrees
# of any node should not be bigger than 1, but he diffence bewteen any
# two leaf nodes can be any number ( maybe smaller than lg(n)?)
class Solution(object):
    def isBalanced(self, root):

    	if not root:
    		return True

    	node_stack = [(root, 0)]

    	levels = []
    	while node_stack:
    		node, level = node_stack.pop()
    		if not node:
    			if level not in levels:
    				if len(levels) == 1 and abs(level - levels[0]) > 1:
    					return False
    				if len(levels) == 2:
    					return False
    				levels.append(level)
    		else:			
				node_stack.append((node.left, level + 1))
				node_stack.append((node.right, level + 1))


    	return True

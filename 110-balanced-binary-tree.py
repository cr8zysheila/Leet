class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isBalanced(self, root):
        return False if self.balanced_height(root) == False else True

    #if root is balanced, return height; else return False
    def balanced_height(self, root):

        if not root:
            return 1

        left_height = self.balanced_height(root.left)
        print root.val, "left_height", left_height
        right_height = self.balanced_height(root.right)
        print root.val, "right_height", right_height

        if left_height == False or right_height == False:
            return False

        if abs(left_height - right_height) > 1:
            return False

        return max(left_height, right_height) + 1


root = TreeNode(1)
root.left = TreeNode(2)
print Solution().isBalanced(root)

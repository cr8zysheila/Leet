class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        #don't use a class variable for last_node, it fails in
        #leetcode when the class is called multiple times for 
        #multiple test cases
        self.last_node = None

    # recursive solution
    def isValidBST(self, root):
        if root == None:
            return True

        if not self.isValidBST(root.left):
            return False

        if self.last_node and self.last_node.val >= root.val:
            return False

        self.last_node = root

        return self.isValidBST(root.right)

    #iterative solution
    def isValidBSTIt(self, root):
        node_stack = []
        curr = root

        while curr != None or node_stack:
            if curr != None:
                node_stack.append(curr)
                curr = curr.left
            else:
                curr = node_stack.pop()
                if self.last_node and self.last_node.val >= curr.val:
                    return False
                self.last_node = curr
                curr = curr.right

        return True


tree = TreeNode(0)

print Solution().isValidBSTIt(tree)

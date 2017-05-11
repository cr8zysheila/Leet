import collections

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    # iterative with queue
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        result = []
        queue = collections.deque()

        if not root:
            return root

        queue.append((root, str(root.val)))
        while queue:
            node, path = queue.popleft()
            if not node.left and not node.right:
                result.append(path)
            if node.left:
                queue.append((node.left, path+'->'+str(node.left.val)))
            if node.right:
                queue.append((node.right, path+'->'+str(node.right.val)))

        return result

    # recursive
    def binaryTreePaths_rec(self, root):
        if not root:
            return []

        result = []
        path = str(root.val)

        self.recursive_path(root, path, result)

        return result

    def recursive_path(self, node, path, result):
        if not node.left and not node.right:
            result.append(path)
        if node.left:
            self.recursive_path(node.left, path+'->'+str(node.left.val), result)
        if node.right:
            self.recursive_path(node.right, path+'->'+str(node.right.val), result)




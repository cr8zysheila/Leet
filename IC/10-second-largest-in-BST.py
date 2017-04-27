class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

node9 = TreeNode(9)
node11 = TreeNode(11)
node10 = TreeNode(10)
node10.left, node10.right = node9, node11
node12 = TreeNode(12)
node12.left = node10
node7 = TreeNode(7)
node4 = TreeNode(4)
node1 = TreeNode(1)
node3 = TreeNode(3)
node3.left, node3.right = node1, node4
node8 = TreeNode(8)
node8.left, node8.right = node7, node12
node5 = TreeNode(5)
node5.left, node5.right = node3, node8

# recursive solution
# return None if the tree has less than 2 nodes
def find_largest(root):
	if not root or not root.right:
		return root
	else:
		return find_largest(root.right)

def find_second_largest(root):

	if not root:
		return root

	if not root.right:
		return find_largest(root.left)
	elif not root.right.left and not root.right.right:
		return root
	else:
		return find_second_largest(root.right)

#iterative solution
def find_largest_it(root):
	if not root:
		return root

	curr = root
	while curr.right:
		curr = curr.right

	return curr


def find_second_largest_it(root):
	curr = root

	while curr:
		if not curr.right:
			return find_largest_it(curr.left)
		elif not curr.right.right and not curr.right.left:
			return curr
		else:
			curr = curr.right

	return curr


print find_second_largest_it(node5).val
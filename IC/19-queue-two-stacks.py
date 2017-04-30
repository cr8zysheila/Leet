class QueueTwoStacks(object):
	def __init__(self):
		self.stack1 = []
		self.stack2 = []

	def push(self, x):
		self.stack1.append(x)

	def stack_move(self):
		while self.stack1:
			self.stack2.append(self.stack1.pop())


	def pop(self):
		last = self.peek()
		self.stack2.pop()
		return last

	def peek(self):
		if not self.stack2:
			self.stack_move()

		if not self.stack2:
			raise Exception("empty queue!")

		return self.stack2[-1]

	def empty(self):
		if not self.stack1 and not self.stack2:
			return True
		else:
			return False


obj = QueueTwoStacks()
obj.push(5)
print obj.peek()
print obj.pop()
print obj.peek()
print obj.empty()
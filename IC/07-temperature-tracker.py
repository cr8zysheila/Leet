class TempTracker(object):
	HIGHEST_TEMP = 110
	def __init__(self):
		self.min_temp = None
		self.max_temp = None
		self.mean = None
		self.mode = None

		self.sum_of_temp = 0.0
		self.nums_of_temps = 0
		self.occurrence = [0] * (TempTracker.HIGHEST_TEMP + 1)

	def insert(self, temp):
		if temp > TempTracker.HIGHEST_TEMP or temp < 0:
			raise Exception('input out of allowed range')

		if not isinstance(temp, int):
			raise Exception('only Integer input is allowed')

		self.sum_of_temp += temp
		self.nums_of_temps += 1
		self.mean = self.sum_of_temp/self.nums_of_temps

		if not self.min_temp or self.min_temp > temp:
			self.min_temp = temp

		if not self.max_temp or self.max_temp < temp:
			self.max_temp = temp

		self.occurrence[temp] += 1
		if not self.mode or self.mode < self.occurrence[temp]:
			self.mode = self.occurrence[temp]

	def get_min(self):
		return self.min_temp

	def get_max(self):
		return self.max_temp

	def get_mean(self):
		return self.mean

	def get_mode(self):
		return self.mode



tt = TempTracker()
tt.insert(66)
tt.insert(77)
tt.insert(88)
tt.insert(66)

print tt.get_min(), tt.get_max(), tt.get_mean(), tt.get_mode()

		




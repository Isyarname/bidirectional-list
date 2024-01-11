class BList:
	def __init__(self, positive=[0], negative=[0]):
		self.positive = positive
		self.negative = negative

	def __str__(self):
		start, end = 0, 0
		for i, e in enumerate(self.positive[-1::-1]):
			if e != 0:
				start = len(self.positive) - i
				break
		for i, e in enumerate(self.negative[-1::-1]):
			if e != 0:
				end = len(self.negative) - i
				break
		return str(self.positive[start-1::-1]+self.negative[:end:])

	def append(self, element=1, in_negative=False):
		if in_negative:
			self.negative.append(element)
		else:
			self.positive.append(element)

	def pop(self, index, x):
		if index < 0:
			self.negative.insert(-index-1)
		else:
			self.positive.insert(index)

	def count(self, x):
		return self.positive.count(x) + self.negative.count(x)

	def reverse(self, index=0):
		if index < 0:
			index = -index - 1
			part1 = self.negative[:index+1]
			part1.extend(self.positive)
			part2 = self.negative[index+1:]
		else:
			part1 = self.positive[index:]
			part2 = self.positive[:index]
			part2.extend(self.negative)
		self.positive = part2
		self.negative = part1

	def insert(self, index, x):
		if index < 0:
			self.negative.insert(-index-1, x)
		else:
			self.positive.insert(index, x)

	def clear(self):
		self.positive.clear()
		self.negative.clear()

	def remove(self, x):
		try:
			self.positive.remove(x)
		except ValueError:
			self.negative.remove(x)

	def extend(self, L: list, in_negative=False):
		if in_negative:
			self.negative.extend(L)
		else:
			self.positive.extend(L)

	def _increase_size(self, length, in_negative=False, element=0):
		self.extend([element]*length, in_negative)

	def _resize(self, index, in_negative=False):
		if in_negative:
			length = len(self.negative) - 1
		else:
			length = len(self.positive) - 1
		if index > length:
			self._increase_size(index-length, in_negative)

	def __getitem__(self, index):
		if index < 0:
			self._resize(-index-1, True)
			return self.negative[-index-1]
		else:
			self._resize(index)
			return self.positive[index]

	def __setitem__(self, index, value):
		if index < 0:
			self._resize(-index-1, True)
			self.negative[-index-1] = value
		else:
			self._resize(index)
			self.positive[index] = value
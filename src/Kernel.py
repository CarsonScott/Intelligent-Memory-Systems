from Functions import subspace, join

class Kernel:

	def __init__(self, size, step, function):
		self.function = function
		self.size = size
		self.step = step

	def __call__(self, space):
		output = []

		for y in range(0, len(space), self.step[1]):
			if y < len(space) - self.size[1]:
				output.append([])
				for x in range(0, len(space[y]), self.step[0]):
					if x < len(space[y]) - self.size[0]:
						S = join(subspace(space, (x, y), self.size))
						output[y].append(self.function(S))
		return output
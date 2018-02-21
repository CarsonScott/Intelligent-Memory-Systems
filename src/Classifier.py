from Functions import compare

class Classifier:
	def __init__(self, patterns):
		self.patterns = patterns

	def __call__(self, pattern):
		output = []
		for i in range(len(self.patterns)):
			output.append(compare(pattern, self.patterns[i]))
		return output.index(max(output))
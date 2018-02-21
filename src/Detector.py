from Functions import distance, offset, sqrt

class Detector:

	def __init__(self, kernel):
		self.kernel = kernel

	def __call__(self, input):
		output = self.kernel(input)
		
		labels = []
		positions = []
		for i in range(len(output)):
			for j in range(len(output[i])):
				if output[i][j] != 0:
					labels.append(output[i][j])
					positions.append((i, j))
	
		pairs = []
		offsets = []
		max_distance = 1.5
		for i in range(len(positions)):
			for j in range(i, len(positions)):
				if i != j:
					if distance(positions[i], positions[j]) <= max_distance:
						pairs.append((i,j))
						offsets.append(offset(positions[i], positions[j]))

		model = {'objects':labels, 'relations':offsets, 'pairs':pairs}
		return model
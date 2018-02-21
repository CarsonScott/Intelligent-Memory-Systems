from Kernel import Kernel
from Classifier import Classifier
from Detector import Detector

input = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		 [0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
		 [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
		 [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
		 [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
		 [0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
		 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

patterns = [[0, 0, 0,
			 0, 0, 0,
			 0, 0, 0],

			[0, 0, 0,
			 1, 1, 1,
			 0, 0, 0],

			[0, 1, 0,
			 0, 1, 0,
			 0, 1, 0]]

classifier = Classifier(patterns)
kernel = Kernel((3,3), (1,1), classifier)
detector = Detector(kernel)

print(detector(input))
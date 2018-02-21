from math import sqrt

def subspace(space, position, size):
	xi = position[0]
	xf = xi + size[0]
	yi = position[1]
	yf = yi + size[1]

	output = []
	for i in range(yi, yf):
		row = []
		for j in range(xi, xf):
			row.append(space[i][j])
		output.append(row)
	return output

def join(X):
	Y = []
	for x in X:
		Y += x
	return Y

def distance(p1, p2):
	x1, y1 = p1
	x2, y2 = p2
	x = pow(x2 - x1, 2)
	y = pow(y2 - y1, 2)
	return sqrt(x + y)

def offset(p1, p2):
	x = p2[0] - p1[0]
	y = p2[1] - p1[1]
	return (x, y)

def sort(X):
	I = []
	for i in range(len(X)):
		I.append(i)
	done = False
	while not done:
		done = True
		for i in range(len(X)-1):
			if X[i] > X[i+1]:
				v = X[i]
				X[i] = X[i+1]
				X[i+1] = v

				z = I[i]
				I[i] = I[i+1]
				I[i+1] = z
				done = False
	return I

def reverse(X):
	Y = []
	for i in range(len(X)-1, -1, -1):
		Y.append(X[i])
	return Y

def compare(x, t):
	y = 0
	for i in range(len(x)):
		y += (x[i] == t[i]) * 1/len(x)
	return y
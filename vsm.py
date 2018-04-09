import numpy as np

def TF(C, mode):
	# mode 0 for max freq
	# mode 1 for BM25
	# C is array of frequency count of terms
	tf = np.zeros(len(C))

	if mode == 0:
		# Maximum frequency normalization	
		# param	
		alpha = 0.5 
		MaxFreq = np.max(C)		

		for i in range(len(C)):
			tf[i] = alpha + (1-alpha) * C[i] / MaxFreq

	elif mode == 1:
		# Okapi/BM25
		# param
		k = 100

		for i in range(len(C)):
			tf[i] = (k+1) * C[i] / (C[i] + k)
	else:
		print('error: TF mode not selected.\n')

	return tf

def IDF():
	# IDF(t) = log(n/k)
	n = 0 # total docs
	k = 0 # docs with term t

	# to-do

	return math.log(n / k, math.e)

def sim(Q, D):
	# calculate the similairty of quary Q and document D 
	# using cosine
	if len(Q) != len(D):
		print('error: dim(Q): ', len(Q), ', dim(D): ', len(D), ' is not same.\n')
		return -1

	upTerm = 0.0
	leftTerm = 0.0
	rightTerm = 0.0
	for j in range(len(D)):
		upTerm += Q[j] * D[j]
		leftTerm += Q[j] * Q[j]
		rightTerm += D[j] * D[j]

	return upTerm / ((leftTerm * rightTerm) ** (0.5))


def main():


if __name__ == '__main__':
	main()

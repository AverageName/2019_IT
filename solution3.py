import numpy as np
import math
from fractions import Fraction

#Find k which k/(1 + split) is integer
def find_num(float_num):
	for i in range(1, 100):
		if i/float_num - int(i/float_num) < 10e-6:
			return i
def get_indices(N, n_batches, split_ratio):
	if N < 1/split_ratio:
		return "This batching is impossible"
	#print(k, n)
	denom = find_num(1 + split_ratio)
	k = denom
	i = 0
	j = k - k/(1 + split_ratio)
	n = k - j
	#print(n)
	for _ in range(n_batches - 1):
		yield np.array([i, j, k])
		j += n
		i = j - split_ratio * n
		k += n
	k = N - 1
	j = k - n
	i = j - split_ratio * n
	yield np.array([i, j, k])

for inds in get_indices(120, 10, 2/7):
	print(inds)
#print(find_num(1/6))

def counting_sort(a, b, k):
	'''
		a: input array
		b: output sorted array
		k: elements in a valued 0..k (1 more than max value)
	'''
	assert a, 'Oops need an array to sort'
	assert b, 'Oops need a b;)'
	assert k, 'need a value for k'
	if len(a) <= 1:
		return a
	# c is counting array, initialize as zeros
	c = [0]*(k)
	for j in range(len(a)):
		# print(j)
		c[a[j]] += 1#c[a[j]] + 1
	# print(c)
	# c now populated with count of elements in 'a'
	for i in range(1,k):
		c[i] += c[i-1]
	# print(c)
	## ^^ c contains count of elements less than equal to i
	for j in reversed(range(len(a))):
		# print(j)
		b[c[a[j]]-1] = a[j]
		# print(a[j], c[a[j]-1], b[c[a[j]]-1])
		c[a[j]] -= 1
	return b


# a = [6,0,2,0,1,3,4,6,1,3,2]
# b = [0]*len(a)
# counting_sort(a,b,k=7)
# print(b)

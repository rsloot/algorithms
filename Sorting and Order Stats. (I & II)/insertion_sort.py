def insertion_sort(a):
	for i in range(1, len(a)):
		key = a[i]
		j = i-1
		# while j is in a and a[j] is greater than the key
		# find the index where key should be inserted
		while j >= 0 and a[j] > key:
			a[j+1] = a[j]
			j -= 1
		a[j+1] = key

# a = [4, 2, 3, 1, 1, 0, 93, 92, 6, 7 ,8]

# print(a)
# insertion_sort(a)
# print(a)
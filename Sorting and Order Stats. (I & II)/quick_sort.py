import random

def quicksort(A, p, r):
	if p < r:
		# q = partition(A,p,r)
		q = randomized_partition(A, p, r)#pivot
		quicksort(A, p, q-1)
		quicksort(A, q+1, r)

def partition(A, p, r):
	# print(A)
	pivot = A[r]
	i = p - 1
	for j in range(p, r):
		# print(pivot, A[j])
		if A[j] <= pivot:
			i += 1
			A[i], A[j] = A[j], A[i]
	A[i+1], A[r] = A[r], A[i+1]
	# print(' '.join(list(map(str, A))))
	# print(i+1)
	# everything above i+1 is greater than i
	return i+1

def randomized_partition(a, p, r):
	i = random.randrange(p,r)
	a[i], a[r] = a[r], a[i]
	return partition(a, p, r)

def quick_sort(a):
	 # returns sorted version of a, but a is not sorted
	if len(a) < 1:
		return a

	pivot = random.choice(a)
	mid = [i for i in a if i == pivot]
	left = quick_sort([i for i in a if i < pivot])
	right = quick_sort([i for i in a if i > pivot])
	
	return left+mid+right

def main():
	random.seed(7)
	a = [random.randint(0,50) for _ in range(12)]
	print(a)
	print(quick_sort(a))
	# print(a)
	quicksort(a, 0, len(a)-1) # in place
	print(a)


if __name__ == '__main__':
    main()
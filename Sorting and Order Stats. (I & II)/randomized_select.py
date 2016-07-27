from random import randint
from quick_sort import randomized_partition

def randomized_select(a, p, r, i):
	assert i > 0, 'i too small'
	if p == r:
		return a[p]
	# returns a semi sorted list
	# values index less than q are less than a[q] in value visa versa
	q = randomized_partition(a,p,r)		#pivot
	k = q - p + 1
	if i == k:
		return a[q]
	elif i < k:
		return randomized_select(a, p, q-1, i)
	else:
		return randomized_select(a, q+1, r, i-k)

def iter_randomized_select(a, p, r, i):
	while p < r - 1:
		q = randomized_partition(a, p, r)
		k = q - p + 1
		if i == k:
			return a[q]
		elif i < k:
			r = q
		else:
			p = q + 1
			i -= k
	return a[p]


def main():
	a = [randint(0,100) for _ in range(10)]
	print(sorted(a))
	el = 2
	el_smallest = iter_randomized_select(a, 0, len(a)-1, el)
	print("the %dnd smallest element in a is %d" % (el, el_smallest))


if __name__ == '__main__':
    main()

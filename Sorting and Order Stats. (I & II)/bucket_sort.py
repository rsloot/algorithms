from math import floor
from insertion_sort import insertion_sort

'''
							** BUCKET SORT **

	runtimes: 
		- Average-case: O(n)
		- Worst-case: O(n^2) -- if all elements in same bucket, we essentially
								have insertion sort.

	assumptions: 
		- input is draw from uniform distribution [0,1)
		- requires auxiliary array b (of linked lists usually--buckets)
			and assumes mechanism for maintaining such lists

	how it works:
		- divides interval, [0,1), into n equal-sized sub-intervals (buckets)
		  then distributes the n inputs into the buckets.
		- since input is unif. and independently distributed over [0,1) we 
		  expect buckets to have few or no numbers (elements) in them.
		- to produce [correct] output sort the numbers in each bucket, then
		  go through the buckets in order (thank linked list), listing elements
		  in each.
'''


def bucket_sort(a):
	n = len(a)
	# b is a list of n empty lists
	# [[]]*n creates copies of same list
	b = [[] for _ in range(n)]
	# print(b[0],len(b), n)
	# b[1].append(5)
	for i in range(n):
		# x = int(floor(n*a[i]))
		# print(b[x])
		b[floor(n*a[i])].append(a[i])
		# print(b[int(floor(n*a[i]))])
	# print(b)
	# insertion sort to sort in-bucket elements
	for i in range(n):
		insertion_sort(b[i])
	# flatten b
	# print(b)
	flat_sorted = [j for i in b for j in i]
	return flat_sorted

a = [.79,.18,.16,.64,.39,.2,.89,.53,.71,.42]
# bucket_sort(a)
print(bucket_sort(a))
# print(a)
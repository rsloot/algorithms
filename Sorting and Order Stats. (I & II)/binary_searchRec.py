def binary_search(list_, value):
	if len(list_) < 2:
		return ValueError('Not Found')

	mid = int(len(list_)/2)

	# print(mid, len(list_))
	if value < list_[mid]:
		return binary_search(list_[:mid], value)
	elif value > list_[mid]:
		return binary_search(list_[mid:], value)
	if list_[mid] == value:
		return (True, mid)
	# return found

import random
random.seed(7)
a = sorted([random.randint(0, 100) for _ in range(100)])
print(a)
print(binary_search(a,7))
print(a[binary_search(a,7)[1]])
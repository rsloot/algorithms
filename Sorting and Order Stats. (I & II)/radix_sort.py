# import merge_sort
from counting_sort import counting_sort


def radix_sort(a, d):
	'''
		a: list to be sorted, will change to strings
		d: number of digits/letters in each element
	'''
	'''
	** TODO **
	
	- will need a (stable) sort modified specifically to take in
		strings. In python cannot index into type int, so need string
		version of number (i.e. '123' rather than 123)
	- Also needed is a way to store sorted values on i index, and somehow
		keep runtime at Big-Theta(n)

	'''
	not_strings = False
	for i in a:
		if type(i) is str:
			continue
		else:
			not_strings = True
	if not_strings:
		a = list(map(str, a))
	for i in reversed(range(d)):
		# use some stable sort to sort list a on digit i
		# example could be counting sort
		# call sorting algo based on ith digit in each element of a
		# merge_sort(a, 0, len(a))
		b = [0]*len(a)
		a = [str(j)[i] for j in a]
		a = counting_sort(list(map(int, a)), b, 4)
		print(a)

a = ['COW','DOG','SEA','RUG','ROW','MOB','BOX','TAB','BAR','EAR','TAR','DIG',
	 'BIG','TEA','NOW','FOX']

a = [301,123,111,222,333,231,213]
print(radix_sort(a, 2))
print(a)
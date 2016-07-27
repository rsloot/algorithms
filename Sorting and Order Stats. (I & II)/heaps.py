class heap(object):
	def __init__(self, heapList=[], heap_size=0):
		self.heapList = heapList
		self.heap_size = heap_size

def left(i):
	return 2*i+1
def right(i):
	return 2*i+2
def parent(i):
	from math import ceil
	return int(ceil(i/2))-1

def max_heapify(a, i):
	'''
	a: a heap :) object
	i: index to heapify
	'''
	l = left(i)#2i+1
	r = right(i)#2i+2
	largest = i
	## change second inequality sign for min heapify
	if l < a.heap_size and a.heapList[l] > a.heapList[largest]:
		largest = l
	if r < a.heap_size and a.heapList[r] > a.heapList[largest]:
		largest = r
	if largest != i:
		a.heapList[i], a.heapList[largest] = a.heapList[largest], a.heapList[i]
		max_heapify(a,largest)

def build_max_heap(a):
	a.heap_size = len(a.heapList)
	for i in range(a.heap_size//2, -1, -1):
		# print(a.heapList, a.heapList[i])
		max_heapify(a,i)

def heap_sort(a):
	build_max_heap(a)
	for i in reversed(range(len(a.heapList))):
		'''
			swapping 'top' element from max_heap, 
			which is the largest element in list, putting it in
			the last position of the heap list, then re-max_heapifying
			the rest of the elements (reducing heapsize by one 'ignores'
			last element in heap list, which is our sorted values) giving
			us the max value at position 0 again and we continue until
			i = 0, and all elements in a are sorted.
		'''
		a.heapList[0], a.heapList[i] = a.heapList[i], a.heapList[0]
		a.heap_size -= 1
		max_heapify(a,0)

def min_heapify(a, i):
	l = left(i)#2i+1
	r = right(i)#2i+2
	smallest = i
	if l < a.heap_size and a.heapList[l] < a.heapList[smallest]:
		smallest = l
	if r < a.heap_size and a.heapList[r] < a.heapList[smallest]:
		smallest = r
	if smallest != i:
		a.heapList[i], a.heapList[smallest] = a.heapList[smallest],a.heapList[i]
		min_heapify(a,smallest)

def build_min_heap(a):
	a.heap_size = len(a.heapList)
	for i in range(a.heap_size//2, -1, -1):
		min_heapify(a, i)


# a = heap([5,3,17,10,84,19,6,22,9])
# for i in range(len(a)//2, -1, -1):
# 	max_heapify(a, i)
# build_max_heap(a)
# print(a.heapList)
# print(heap_sort(a))
# print(a.heapList)

# print(a.heapList)
# build_min_heap(a)
# print(a.heapList)
from heaps import *#heap, left, right, parent

def heap_maximum(a):
	## assuming a is max heap
	assert type(a) is heap, 'parameter should be a max_heap'
	assert a.heapList[0] == max(a.heapList), \
						"Incorrect, make sure it is a max heap"
	return a.heapList[0]

## testing heap_maximum
# a = heap([3,2,1,4,5,62,1,4,3])
# build_max_heap(a)
# print(heap_maximum(a))

def heap_extract_max(a):
	## assuming max_heap
	assert type(a) is heap, "not a heap"
	assert a.heap_size >= 1, 'ERROR: heap underflow'
	max_ = a.heapList.pop(0)
	# a.heapList[0] = a.heapList[a.heap_size-1]
	a.heap_size -= 1
	max_heapify(a, 0)
	return max_

# # testing heap_extract_max
# a = heap([3,2,1,4,5,62,1,4,3])
# build_max_heap(a)
# print(a.heapList)
# print(heap_extract_max(a))
# print(a.heapList)

def heap_increase_key(a, i, key):
	## make sure heap and new key > current
	assert type(a) is heap, 'not a heap'
	assert key > a.heapList[i], 'new key is smaller than current key'
	a.heapList[i] = key
	while i > 0 and a.heapList[parent(i)] < a.heapList[i]:
		a.heapList[i], a.heapList[parent(i)] = \
									a.heapList[parent(i)], a.heapList[i]
		i = parent(i)

# # Testing heap_increase_key
# a = heap([4,3,2,5,76,94,3,7,8])
# build_max_heap(a)
# print(a.heapList)
# heap_increase_key(a, 6, 99)
# print(a.heapList)

def max_heap_insert(a, key):
	## make sure 'a' is heap 
	assert type(a) is heap, 'not a heap'
	# increase heap_size by 1 to add new element
	a.heap_size += 1
	## set last element to -inf, then we call
	a.heapList.append(float('-inf'))
	## increase_key with our key and last element index
	heap_increase_key(a, a.heap_size-1, key) 

# # Testing max_heap_insert
# a = heap([4,3,2,5,76,94,3,7,8])
# build_max_heap(a)
# print(a.heapList)
# max_heap_insert(a, 6)
# print(a.heapList)

################################
''' MIN HEAP Priority Queues '''
################################
def heap_min(a):
	# assume min_heap
	assert type(a) is heap, 'not a heap'
	assert a.heapList[0] == min(a.heapList), 'Not min->not a min_heap'
	return a.heapList[0]

## Test heap min
# a = heap([2,45,7,8,9,3,3,6,7,2,7,9,10])
# build_min_heap(a)
# print(heap_min(a))

def heap_extract_min(a):
	# get min and remove from heap
	assert type(a) is heap, IOError("not a heap")
	assert a.heap_size >= 1, 'ERROR: heap underflow'
	min_ = a.heapList.pop(0)
	# a.heapList[0] = a.heapList[a.heap_size-1]
	a.heap_size -= 1
	# min_heapify(a, 0)##not a min heap
	build_min_heap(a)
	return min_

## Test heap_extract_min
# a = heap([3,432,5,3,5,5,325,4,2,1,9,8,0])
# build_min_heap(a)
# print(a.heapList)
# print(heap_extract_min(a))
# print(a.heapList)

def heap_decrease_key(a, i, key):
	## make sure heap and new key > current
	assert type(a) is heap, 'not a heap'
	assert key < a.heapList[i], 'new key is bigger than current key'
	a.heapList[i] = key
	while i > 0 and a.heapList[parent(i)] > a.heapList[i]:
		a.heapList[i], a.heapList[parent(i)] = \
									a.heapList[parent(i)], a.heapList[i]
		i = parent(i)

## Testing heap_decrease_key
# a = heap([4,3,2,5,76,94,3,7,8])
# build_min_heap(a)
# print(a.heapList)
# heap_decrease_key(a, 6, 0)
# print(a.heapList)

def min_heap_insert(a, key):
	## make sure 'a' is heap 
	assert type(a) is heap, 'not a heap'
	# increase heap_size by 1 to add new element
	a.heap_size += 1
	## set last element to inf, then we call
	a.heapList.append(float('inf'))
	## increase_key with our key and last element index
	heap_decrease_key(a, a.heap_size-1, key)

## Testing min_heap_insert
# a = heap([2,54,8,5,23,9,0,12,15,33,1])
# build_min_heap(a)
# print(a.heapList)
# min_heap_insert(a, 3)
# print(a.heapList)

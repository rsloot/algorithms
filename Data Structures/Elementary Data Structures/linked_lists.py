
class Element(object):
	def __init__(self, key):
		self.key = key
		self.prev = None
		self.next = None

class Doubly_linked_list(object):
	def __init__(self, head=None):
		self.head = head
		self.tail = head

	def append(self, new_element):
		current = self.head
		prev = self.head
		i = 0
		if self.head:
			while current.next:
				current = current.next
				i+=1
				if i > 0:
					current.prev = prev
					prev = current
			new_element.prev = current
			current.next = new_element
			self.tail = new_element
		else:
			self.head = new_element

	def search(self, k):
		if self.head:
			x = self.head
			while x and x.key!=k:
				x = x.next
			return x

	def insert(self, x):
		x.next = self.head
		if self.head:
			self.head.prev = x
		self.head = x

	def delete(self, x):
		if x ==None:
			return
		if x.prev:
			x.prev.next = x.next
		else:
			self.head = x.next
		if x.next:
			x.next.prev = x.prev

	def delete_by_key(self, key):
		x = self.search(key)
		self.delete(x)


class Sentinal_dll(object):
	def __init__(self, element=None):
		self.none = Element(None)
		if element:
			self.none.next = element
			element.prev = self.none
			self.none.prev = element
		else:
			self.none.next = self.none.prev
			self.none.prev = self.none.next

	def insert(self, x):
		x.next = self.none.next
		self.none.next.prev = x
		self.none.next = x
		x.prev = self.none

	def search(self, k):
		x = self.none.next
		self.none.key 		# lets us 
		while x.key!=k:		# get rid of x != self.none
			x = x.next
		return x

	def delete(self, x):
		x.prev.next = x.next
		x.next.prev = x.prev

	def delete_by_key(self, key):
		x = self.search(key)
		self.delete(x)


class linked_list(object):
	def __init__(self, head=None):
		self.head = head

	def insert(self, x):
		x.next = self.head
		self.head = x

	def search(self, k):
		x = self.head
		while x.next and x.key != k:
			x = x.next
		return x

	def delete(self, x):
		# key = self.seach(x)
		cur = self.head
		prev = None
		while cur.value != value and cur.next:
			prev = cur
			cur = cur.next
		if cur.value == value:
			if prev:
				prev.next = cur.next
			else:
				self.head = cur.next


	### building a stack operations ###
	def push(self, el):
		if self.head:
			el.next = self.head
			self.head = el
		else:
			self.head = el

	def pop(self):
		x = self.head
		self.head = self.head.next
		return x

	### queue operations ###
	def enqueue(self, el):
		# appending
		if self.head == None:
			self.head = el
			return
		x = self.head
		# loop to last element and add new element to next attribute
		while x.next:
			x = x.next
		x.next = el

	def dequeue(self):
		# or self.pop()
		x = self.head
		self.head = self.head.next
		return x


def main():
	# Doubly Linked Lists
	print('*Testing: Doubly Linked List implementation')
	dll = Doubly_linked_list(Element(0))
	dll.append(Element(32))
	dll.append(Element(7))
	dll.append(Element(22))

	dll.insert(Element(1))

	dll.delete_by_key(0)

	# print(dll.head.key)
	# print(dll.head.next.key)
	# print(dll.head.next.prev.key)
	test_vals = []
	x0 = dll.tail
	print(x0.key)
	test_vals.append(x0.key)
	while x0.prev:
		x0 = x0.prev
		test_vals.append(x0.key)
		print(x0.key)

	correct_values = [22,7,32,1]
	assert test_vals == correct_values, 'Incorrect values'
	assert len(test_vals) == len(correct_values), 'Incorrect length'
	print('passed :)')


	# Sentinal testing
	print('\n*Testing*: Sential doubly linked lists')
	a = [Element(1), Element(2), Element(3), Element(4)]
	dlls = Sentinal_dll(Element(0))
	for i in reversed(a):
		dlls.insert(i)
	
	x1 = dlls.none.next
	i=0
	print(x1.key)
	sent = [x1.key]
	dlls.delete_by_key(4)

	while x1.next:
		x1 = x1.next
		sent.append(x1.key)
		print(x1.key)

	assert sent == [1,2,3,0], "Incorrect"
	print('passed :)')

	# Stack using singly Linked List
	print('\n*Testing*: Stack using singly Linked List')
	ll = linked_list(Element(0))
	a = [Element(1), Element(2), Element(3), Element(4)]
	
	for i in reversed(a):
		ll.push(i)

	ll.pop()
	ll.push(Element(91284091))
	x2 = ll.head
	print(x2.key)
	stack_v = [x2.key]
	while x2.next:
		x2 = x2.next
		print(x2.key)
		stack_v.append(x2.key)

	assert stack_v == [91284091,2,3,4,0], 'Incorrect :('
	print('passed :)')



	# Testing queue implementation using singly linked list
	print('\n*Testing*: queue operations using linked list')
	ll = linked_list(Element(0))
	a = [Element(1), Element(2), Element(3), Element(4)]
	for i in a:
		ll.enqueue(i)
	ll.dequeue() # removing 0

	ll.enqueue(Element(7)) # adding 7 to end of list

	x3 = ll.head
	queue = [x3.key]
	print(x3.key)
	while x3.next:
		x3 = x3.next
		print(x3.key)
		queue.append(x3.key)

	assert queue == [1,2,3,4,7], ':('
	print('passed :)')

if __name__ == '__main__':
	main()
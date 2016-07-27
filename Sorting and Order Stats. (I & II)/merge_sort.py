def merge_sort(a):
	if len(a) > 1:
		mid = int((len(a))/2)
		left = merge_sort(a[:mid])#, 0, mid)
		right = merge_sort(a[mid:])#, mid+1, len(a))
		merge_(a, left, right)
	return a

''''
	Merging with sentinal values 
	(adding infinity to ends of left and right lists)
'''
def merge(a, left, right):
	left.append(float('inf'))
	right.append(float('inf'))
	i = 0
	j = 0
	for k in range(len(a)):#len(left)-1+len(right)-1):
		if left[i] <= right[j]:
			a[k] = left[i]
			i += 1
		else:
			a[k] = right[j]
			j+=1

'''Merge without sentinal values'''
def merge_(a, left, right):
	i = 0
	j = 0
	for k in range(len(a)):
		if left[i] <= right[j]:
			a[k] = left[i]#left.pop(i)
			i += 1
		else:
			a[k] = right[j]#right.pop(i)
			j+=1
		if j>=len(right) and i < len(left):
			# if right side empty but still values in left
			# add remaining values from left to main list
			while i<len(left):
				k+=1
				a[k] = left[i]
				i+=1
			break
		elif i >=len(left) and j < len(right):
			# if left side empty but sill values in right
			# add remaining values from right to main list
			# since already sorted can just add one-by-one
			while j < len(right):
				k+=1
				a[k] = right[j]
				j+=1
			break


# a = [5,3,10, 9, 732,12,2,2,1,6,7,3,63,0, -1, 3.5]
# merge_sort(a)#,0,len(a))
# print(a)
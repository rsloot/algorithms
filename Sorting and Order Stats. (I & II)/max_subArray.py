'''
max sub array problem

	example: find maximum profit given stock 
	data for 17 days, can buy/sell whenever.
	must buy before sell (day buy must be <
	the day you sell)

	divide and conquer
'''

def max_crossing(a, low, mid, high):
	left_sum = float('-inf')
	sum_ = 0
	max_left = 0
	for i in reversed(range(low, mid)):
		sum_ += a[i]
		if sum_	> left_sum:
			left_sum = sum_
			max_left = i
	right_sum = float('-inf')
	sum_ = 0
	max_right=0
	for j in range(mid, high):
		sum_ += a[j]
		if sum_ > right_sum:
			right_sum = sum_
			max_right = j
	return (max_left, max_right, left_sum+right_sum)

from math import floor
def max_sub_array(a, low, high):
	if low == high:
		return(low, high, a[low-1])		#base case one-element
	else:
		mid = int(floor(low+high)/2)
		(low_left, high_left, left_sum) = max_sub_array(a, low, mid)
		(low_right, high_right, right_sum) = max_sub_array(a, mid+1, high)
		(low_cross, high_cross, cross_sum) = max_crossing(a, low, mid, high)
		## check which one is biggest
		if left_sum >= right_sum and left_sum >= cross_sum:
			return (low_left, high_left, left_sum)
		elif right_sum >= left_sum and right_sum >= cross_sum:
			return (low_right, high_right, right_sum)
		else:
			return (low_cross, high_cross, cross_sum)


## return 8->11 $43 (zero based 7->10)
a = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -9, 7]
# a = [-3]*8
print(max_sub_array(a, 0, len(a)))

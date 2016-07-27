# where T is binary search tree
def print_tree(T):
	x = T.root
	if x != None:
		print_tree(x.left)
		print(x.key)
		print_tree(x.right)

## non-recursive, using stack as auxiliary data structure
## T is binary tree
## S is stact
def print_tree(T, S):
	S.push(T.root)
	while not stack_empty(S):
		x = S[S.top]
		while x != None:	# store all nodes on the path towards leftmost leaf
			S.push(x.left)
			x = S[S.top]
		S.pop()				# S has None on its top, so pop
		if not stack_empty(S):
			x = S.pop()
			print x.key
			S.push(x.right)
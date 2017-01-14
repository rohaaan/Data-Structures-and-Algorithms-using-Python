import os
import sys

def recursive_fun(arg):
	if 0 == arg:
		return
	recursive_fun(arg - 1)
	print arg

def iterative_fun(arg):
	stack = []
	stk_idx = 1
	push = True

	while stk_idx > 0:
		if 0 == arg:
			push = False
			stk_idx -= 1

		if push:
			stack.append(arg)
			stk_idx += 1
			arg -= 1
		elif not push:
			arg = stack.pop()
			print arg
			stk_idx -= 1

if __name__ == "__main__":
	print "Recursive"
	recursive_fun(10)
	raw_input()
	print "Iterative"
	iterative_fun(10)
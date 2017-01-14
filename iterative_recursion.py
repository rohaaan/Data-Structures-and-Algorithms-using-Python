#===============================================================================
# Name: Iterative_Recursion
# Purpose: Demonstrate implementation of recursion using iterations.
# Note for other contributors: Do not forget to <<Update>> the 'History' block.
# History:
# 	Date: 14 Jan 2017
#	Author: Rohan Kumbhar
#	Remarks: Created
#===============================================================================

#=================
# Imports section
#=================
import os
import sys

#========================
# Function definitions
#========================
def recursive_fun(arg):
	'''
	Function name: recursive_fun
	Argument: arg
	Description: integer value describing max in range 1 to arg.
	Return value: None
	Purpose: Print numbers from 1 to arg recursively.
	'''
	if 0 == arg:
		return
	recursive_fun(arg - 1)
	print arg

def iterative_fun(arg):
	'''
	Function name: iterative_fun
	Argument: arg
	Description: integer value describing max in range 1 to arg.
	Return value: None
	Purpose: Print numbers from 1 to arg by implementing iterative recursion.
	'''
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

#======================
# Script entry point.
#======================
if __name__ == "__main__":
	print "Recursive"
	recursive_fun(10)
	raw_input()
	print "Iterative"
	iterative_fun(10)

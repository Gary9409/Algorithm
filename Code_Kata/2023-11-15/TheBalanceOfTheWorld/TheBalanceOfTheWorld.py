import sys

input = sys.stdin.readline
left = {'(', '['}
right = {')', ']'}

def solution(str):
	for c in str:
		if c == '.':
			break
		elif c not in left and c not in right:
			continue
		elif c in left:
			stack.append(c)
		elif valid(stack, c):
			stack.pop()
		else:
			return False
	return stack == []

def valid(stack, c2):
	if not stack:
		return False

	c1 = stack[-1]
	if c1 == '(' and c2 == ')':
		return True
	elif c1 == '[' and c2 == ']':
		return True
	return False

while True:
	stack = []
	s = input().rstrip()
	if s == ".":
		break
	print("yes") if solution(s) else print("no")
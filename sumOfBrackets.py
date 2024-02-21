tests = int(input())
for _ in range(tests):
	n = int(input())
	x = float(input())
	ans = n*int(x)
	remainToTwo = int(x)+1 - x
	secondround = int(remainToTwo*n + 1) + 1 
	secondround = n - secondround
	print(ans + secondround+ 1)
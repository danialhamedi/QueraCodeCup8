n, v = map(int, input().split())
arr = []
for _ in range(n):
	arr.append(tuple(map(int, input().split())))
arr = sorted(arr, key= lambda x: -x[0]/x[1])
remainingV = v
totalH = 0
for elem in arr :
	if remainingV == 0:
		break
	elif remainingV > elem[1]:
		totalH += elem[0]
		remainingV -= elem[1]
	else:
		coef = remainingV / elem[1]
		totalH += coef * elem[0]
print(int(totalH*10)/10)

L = [1,2,4,8,16,32,64]
X = 5

#list index method
for num in L:
	if 2**X == num:
		print('at index',L.index(num))
		break
else:
	print(X, 'not found')

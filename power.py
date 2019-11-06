#Generating powers-of-2 list L
L = []
for i in range(6):
	L.append(2**i) 

print(L)
X=5
if 2**X in L:
	print('at index',L.index(2**X))
else:
	print(X, 'not found')

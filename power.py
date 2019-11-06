#for-else construction
print('for-else construction')

for i in range(len(L)):
	if 2**X == L[i]:
		print('at index', i)
		break
	else:
		i = i+1
else:
	print(X, 'not found')

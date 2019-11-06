#keyword argument
def adder(good = 1, bad = 2, ugly = 3):
	return(good+bad+ugly)

print(adder(ugly = 1, good = 5)) #The result will be 5+2+1 = 8

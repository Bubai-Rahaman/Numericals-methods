# generalise for urbitrary number of arguments

def adder(**kwargs):
	L = list(kwargs.values())
	sum = 0
	for i in L:
		sum+=i
	return(sum)

print(adder(day = 24, jan = 6, sec= 1, gd= 4))

#generalise adder function
def gen_adder(*argv):
	sum = 0
	for arg in argv:
		sum+=arg
	return(sum)

print(gen_adder(1,2,3,4,5))

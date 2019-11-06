#module
def fib(n):

	if n<0:
		print("Please enter a postive integer...")
	
	elif n==0:
		print(0)

	elif n>0:
		a = 0
		b = 1

		print(a)

		for i in range(n-1):
			c = a+b
			print(c)
			a=b
			b=c	
	return


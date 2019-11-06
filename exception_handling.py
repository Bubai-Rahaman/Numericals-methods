'''
Name: Bubai Rahaman
'''

for i in range(5):
	try:
		x=1/i
		print("1/", i ,"=",x)

	except ZeroDivisionError:
		print("indeterminate")

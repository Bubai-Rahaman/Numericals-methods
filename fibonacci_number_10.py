#time
import timeit

mycode = '''
import module_fib
module_fib.fib(100)
'''

print("Time required to print 100 fibonacci numbers is =", (timeit.timeit(stmt = mycode,number = 100))/100,"sec")

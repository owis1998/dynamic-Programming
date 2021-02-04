def fib(n):
	if n <= 2 :
		return n
	
	val = fib(n - 1) + fib(n - 2)
	return val

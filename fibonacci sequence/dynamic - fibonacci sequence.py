dic = {} 

def fib(n):
	if n <= 2 :
		return n

	if n in dic:
		return dic[n]
	
	val = fib(n - 1) + fib(n - 2)
	dic[n] = val
	return val

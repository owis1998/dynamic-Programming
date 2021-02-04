def algorithm(val, lst):
	memo = {}
	def f(val):		
		if val == 0:
			if minimum_coin[0] > len(stack):
				minimum_coin[0] = len(stack) 
				minimum_coin[1] = stack.copy()
			return

		for i in lst:
			if i <= val:
				stack.append(i)
				f(val - i)
				stack.pop()


	for n in range(0, val + 1):
		sub = []
		for l in lst:
			if n < min(lst):
				memo[n] = 0
				break

			if n < l:
				continue

			if n - l in memo:
				sub.append(memo[n - l] + 1)
			else:
				stack = []
				minimum_coin = [val + 1, []]
				f(n)
				sub.append(minimum_coin[0] + 1)
		else:
			memo[n] = min(sub)

	return memo[val]

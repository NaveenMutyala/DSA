def maximumValue(items, n, w):

	# Write your code here.
	# ITEMS contains [weight, value] pairs.
	# pass
	items.sort(key = lambda x: x[1]/x[0],reverse = True)
	val =0
	for i in items:
		if w==0:
			break
		if i[0]<=w:
			val+=i[1]
			w-=i[0]
		else:
			val+=(i[1]/i[0])*w
			w=0
	return val


# Sample Input 1:
# 1
# 6 200
# 50 40 90 120 10 200 
# 40 50 25 100 30 45
# Sample Output 1:
# 204.00

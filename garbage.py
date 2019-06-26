

def mySqrt(x):
	if x==1:return 1
	l=0
	r=x
	while 1<=r:
		mid=(r+1)//2
		if mid*mid <=x<(mid+1)*(mid+1):
			return mid
		elif x<mid*mid:
			r=mid
		else:
			l=mid
print(mySqrt(12379237))
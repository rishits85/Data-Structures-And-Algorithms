# Uses python3
import sys

# in this recursive algorithm, the key is the modulo of first number with second number. Key is one who needs to be changed until reaching a break point in algo. This key should
# relate our need with constantly changing entity
def gcd_naive(a, b):
	if(b==0):
		return a
	elif(a==0):
		return b
	else:
		if(b>a):
			aPrime = b % a
			return gcd_naive(aPrime, a)
		else:
			aPrime = a%b
			return gcd_naive(b,aPrime)


if __name__ == "__main__":
		input = input()
		a, b = map(int, input.split())
		print(gcd_naive(a,b))
		


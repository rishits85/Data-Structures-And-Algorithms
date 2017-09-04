# Uses python3
import sys


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

def lcm_naive(a, b):
	gcd = gcd_naive(a,b)
	lcm = (a*b)//gcd
	return lcm

if __name__ == '__main__':
    myInput = input()
    a, b = map(int, myInput.split())
    print(lcm_naive(a, b))


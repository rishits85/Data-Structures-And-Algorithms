# Uses python3

import sys

# n = sys.stdin.read()
import random
def fib_fast(n):
    arr = []
    if (n < 0):
        return ("invalid input. Please enter a valid positive number")
    else:
        for x in range(0,n+1):
            if (x>1):
                y = arr[x-1] + arr[x-2]
                arr.append(y)
            else:
                arr.append(x)
        return arr[n]


if __name__ == '__main__':
    n = int(input())
    print(fib_fast(n))
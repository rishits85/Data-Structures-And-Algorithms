# Uses python3
import sys

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    myLength = get_length(m)
    fibo = get_fibo(n%myLength)
    return fibo%m



    
        
def get_length(m):
    a = 0
    b = 1
    c = a+b
    for i in range (0,m*m):
        c = (a + b) % m
        a = b
        b = c
        if(a == 0 and b == 1):
            return i+1

def get_fibo(n):
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
    input = input()
    n, m = map(int, input.split())
    print(get_fibonacci_huge_naive(n, m))

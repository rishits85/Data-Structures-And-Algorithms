# Uses python3
import sys
import random
#n = int(input())
def get_fibonacci_last_digit_naive(n):
    if (n < 0):
        return ("invalid input. Please enter a valid positive number")
    elif (0<= n <=60):
        return (getLast(n))
    else:
        y = (n//60) * 60
        n = n - y
        return(getLast(n))


def getLast(n):
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
        return arr[n] % 10


if __name__ == '__main__':
    n = int(input())
    print(get_fibonacci_last_digit_naive(n))
    #print(get_fibonacci_last_digit_naive(x))


# Uses python3
import sys

   
def fibonacci_sum_naive(n):
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
        for x in range(0,n+3):
            if (x>1):
                y = arr[x-1] + arr[x-2]
                arr.append(y)
            else:
                arr.append(x)
        # print(arr[n+2] % 10)    
        if(arr[n+2]%10 == 0):
            return(9)
        else:
            return (arr[n+2] % 10) -1 

if __name__ == '__main__':
    input = input()
    n = int(input)
    print(fibonacci_sum_naive(n))


    #0 1 2 3 4 5 6 7    8   9   10   11    12    13    14    15 
    #0 1 1 2 3 5 8 13  21  34  55   89   144   233   377   610
    #0 1 2 4 7 12 20 33 54 89 144  233   377   610 


# sum F(n) = F(n+2) - 1 
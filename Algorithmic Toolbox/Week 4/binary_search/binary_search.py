# Uses python3
import sys

# key here is the left and right, which vary around half
def binary_search(a, x, left, right):
    # write your code here\
    half = left + (right - left )//2
    if right < left:
        return -1
    if(x == a[half]):
        return half
    elif(x < a[half]):
        return binary_search(a,x,left, half - 1)
    elif(x > a[half]):
        # print(right)
        return binary_search(a,x, half + 1, right)

    # while(left <= right):
    #     if(left >= len(a)):
    #         return -1
    #     else:
    #         if((left == right) and a[left] != x):
    #             print("lft and right equal")
    #             return -1
    #         half = (left + right)//2
    #         if a[half] == x:
    #             print("x equal")
    #             return half
    #         elif a[half] < x:
    #             print("x greater")
    #             left = half + 1
    #             print("left")
    #             print(left)
    #         elif a[half] > x:
    #             print("x smaller")
    #             right = half -1
    #             print("right")
    #             print(right)

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    # x = 11
    left = 0
    right = len(a) - 1
    # print(binary_search(a,x,left, right), end = '')
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, x, left, right), end = ' ')

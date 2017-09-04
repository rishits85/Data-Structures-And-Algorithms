# Uses python3
import sys

def get_majority_element(a, left, right):
    # if left == right:
    #     return -1
    # if left + 1 == right:
    #     return a[left]
    my_dict = dict()
    #write your code here
    for i in range (left, right):
        # print(a[i])
        if a[i] in my_dict:
            # print("a[i] in dict")
            my_dict[a[i]] +=1
            # print(right//2)
            # print(my_dict[a[i]])
            if(my_dict[a[i]] > right//2):
                # print("my_dict is larger")
                # print(right/2)
                return 1
                break
        else:
            my_dict[a[i]] = 1
            # print (my_dict)
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)

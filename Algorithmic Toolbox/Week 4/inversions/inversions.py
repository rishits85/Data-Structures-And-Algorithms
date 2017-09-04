# Uses python3
import sys
# key is the one/two varying factors that can be reduced to a value which is breaking point for recursion to stop and is related to the solution. 
# The key here is midpoint of the array. It can be broken until it is the only element in the array. It is related to the number of inversions by acting
# as pivot for doing inversions on its left and right side for sortings
def get_number_of_inversions(a,b,count):
    print (b)
    result = []
    if len(a) <= 1:
        return sorted(a)
    mid = int(len(a) / 2)
    y = get_number_of_inversions(a[:mid],b,count)
    print("y")
    print(y)
    
    z = get_number_of_inversions(a[mid:],b,count)
    print("z")
    print(z)
    i = 0
    j = 0
    while i < len(y) and j < len(z):
        if y[i] > z[j]:
            result.append(z[j])
            j += 1
        else:
            result.append(y[i])
            i += 1
    result += y[i:]
    result += z[j:]
    b[1] += j
    # result.append(count)
    return result

def merge(m,n):
    for i in len(m):
        b.append(min(m[i],n[i]))
        b.append(max(m[i],n[i]))

    return b

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n*[0]
    count = 0
    m, *c = list(map(int,input.split()))
    mycount = get_number_of_inversions(a,b,count)
    # print(mycount)
    # print(mycount[len(a)])
    


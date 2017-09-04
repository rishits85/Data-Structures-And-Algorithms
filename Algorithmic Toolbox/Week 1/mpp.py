# Uses python3
n = int(input())
a = [int(x) for x in input().split()]
#assert means check the condition and trigger an error if it is wrong
assert(len(a) == n)

result = 0


max_index_1 = -1
for j in range(0,n):
    if(max_index_1 == -1 or a[j] > a[max_index_1]):
        max_index_1 = j

max_index_2 = -1
for j in range(0,n):
    if((max_index_2 == -1 or a[j] > a[max_index_2]) and j != max_index_1):
        max_index_2 = j
        

result = a[max_index_1]*a[max_index_2]    

print(result)

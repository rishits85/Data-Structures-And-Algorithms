# Uses python3
import sys

def optimal_sequence(n):
    v = [0] * (n+1)
    v[1] = 1
    # print(v)
    for i in range(1,n):
        if v[i+1] == 0 or v[i + 1] > v[i] +1: v[i+1] = v[i] + 1
        if(i*2<n+1):
            if v[i*2] == 0 or v[i*2] > v[i] +1: v[i*2] = v[i] + 1
        if(i*3<n+1):
            if v[i*3] == 0 or v[i*3] > v[i] +1: v[i*3] = v[i] + 1
    solution = []
    while n > 1:
        # print(n)
        solution.append(n)
        if v[n-1] == v[n] - 1: 
            n = n-1
            # print(n)
        elif n%2 == 0 and v[n//2] == v[n] -1: 
            n = n//2
            # print(n)
        elif n%3 == 0 and v[n//3] == v[n] -1: 
            n = n//3
            # print(n)
    solution.append(1)
    # print(v)
    return solution

        

# def greedy_sequnce(n):
#     sequence = []
#     while n >= 1:
#         sequence.append(n)
#         if n % 3 == 0:
#             n = n // 3
#         elif n % 2 == 0:
#             n = n // 2
#         else:
#             n = n - 1
#     return (len(sequence) -1)

input = sys.stdin.read()
n = int(input)
# steps =optimal_sequence(n)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')


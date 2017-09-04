# Uses python3
import sys

def optimal_weight(W, w, n):
    # write your code here
    value = [[0 for x in range(n+1)] for y in range(W+1)]
    # print(value)
    # print(w)
    for i in range(0,n+1):
    	# print(i)
    	for j in range(0,W+1):
    		# print(j)
    		# print(i)
    		value[j][i] = value[j][i-1]
    		if w[i-1] <= j:
    			val = value[j-w[i-1]][i-1] + w[i-1]
    			if value[j][i] < val:
    				value[j][i] = val
    # print(value)
    return value[W][n]
# def greedy():
# 	result = 0
#     for x in w:
#         if result + x <= W:
#             result = result + x
#     return result

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w, n))

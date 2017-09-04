# Uses python3
def edit_distance(s, t):
    #write your code here

    d = [[0 for j in range(len(s)+1)] for i in range(len(t)+1)]
    # print (d)
    for j in range(1,len(s)+1):
    	d[0][j] = j
    for i in range(1,len(t)+1):
    	d[i][0] = i

    for i in range (1,len(t)+1):
    	for j in range(1,len(s)+1):
    		# if(i == 1):
    			# print(i)
    			# print(j)
    		insertion = d[i][j-1] +1
    		deletion = d[i-1][j] + 1
    		match = d[i-1][j-1]
    		mismatch = d[i-1][j-1] + 1
    		# if(j == 6 and i ==5):
    		# 	print("j is 6")
    		# 	print(j)
    		# 	print(insertion)
    		# 	print(deletion)
    		# 	print(match)
    		# 	print(mismatch)
    		if(s[j-1] == t[i-1] ):
    			d[i][j] = min(insertion, deletion, match)
    		else:
    			d[i][j] = min(insertion,deletion,mismatch)
    # print(d)
    # print(len() -1)
    # print(len(t) -1)
    return (d[len(t)][len(s)])

if __name__ == "__main__":
    print(edit_distance(input(), input()))
    # edit_distance(input(), input())

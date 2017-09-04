#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size
boolean = True
result_inOrder = [] 

def IsBinarySearchTree(key,left,right,node):
  # Implement correct algorithm here
  # if left[node] == -1 and right[node] == -1:
  #   pass
  # else:
  #   print(key[left[node]])
    
  #   if(key[left[node]] > key[node] or key[left[node]] < key[0]):
  #       boolean = False
  #   print(key[right[node]])
  #   if(key[right[node]] < key[node] or key[right[node]] < key[0] ):
  #     print("right eror")
  #     boolean = False
  #   if(right[node] != -1 ):
  #     return IsBinarySearchTree(key,left,right,right[node])
  #   # else:
  #   #   retur
  # return True
  boolean = True
  result ,myIndex= inOrder(key,left,right,node)
  # print(result)
  # print(result)
  # print(myIndex)
  for i in range(0,len(result) - 1):
    # print(myIndex)
    if result[i] > result[i+1]:
      # print("left eror")
      return  False
  return True


def inOrder(key,left,right,node):
  key_index = 0
  # Finish the implementation
  # You may need to add a new recursive method to do that
  if left[node] == -1 and right[node] == -1:
    result_inOrder.append(key[node])
    return
  else:
    if(left[node] != -1):
      inOrder(key,left,right,left[node])
    result_inOrder.append(key[node])
    if key[node] == key[0]:
      key_index = len(result_inOrder)- 1
      # print(key_index)
      # print(result_inOrder.index(4))
    if(right[node] != -1):
      inOrder(key,left,right,right[node])
  return(result_inOrder,key_index)

def main():
  n = int(sys.stdin.readline())
  key = [0 for i in range(n)]
  left = [0 for i in range(n)]
  right = [0 for i in range(n)]
  for i in range(n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      key[i] = a
      left[i] = b
      right[i] = c
  # print(key)
  # print(left)
  # print(right)
  if(n == 0 or n==1):
    print("CORRECT")
  else:
    if IsBinarySearchTree(key,left,right,0):
      # print(IsBinarySearchTree)
      print("CORRECT")
    else:
      print("INCORRECT")

threading.Thread(target=main).start()

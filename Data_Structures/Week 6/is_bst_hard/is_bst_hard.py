#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size
boolean = True
result_inOrder = [] 

# class Node(key,left,right):
#   self.data = 

class BST():
  def IsBinarySearchTree(self,minimum,node,maximum,key,left,right):
    
    # print("minimum")
    # print(minimum)
    # print("max")
    # print(maximum)
    # print("key")
    # print(key)
    # print("left")
    # print(left)
    # print("right")
    # print(right)
    # print("node")
    # print(node)
    if node == -1:
      return True
    else:
      if (key[node] < minimum or key[node] >= maximum):
        # print("compare error")
        return False
      else:
          return self.IsBinarySearchTree(minimum,left[node],key[node],key,left,right) and self.IsBinarySearchTree(key[node],right[node],maximum,key,left,right)


    
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
    # print(-sys.maxsize)
    # minimum = -sys.maxsize
    mybst = BST()
    # print(mybst.IsBinarySearchTree(-sys.maxsize,0,sys.maxsize,key,left,right))
    if mybst.IsBinarySearchTree(-sys.maxsize,0,sys.maxsize,key,left,right):
      print("CORRECT")
    else:
      print("INCORRECT")

threading.Thread(target=main).start()








# def inOrder(key,left,right,node):
#   key_index = 0
#   # Finish the implementation
#   # You may need to add a new recursive method to do that
#   # print(node)
#   if left[node] == -1 and right[node] == -1:
#     result_inOrder.append(key[node])
#     return
#   else:
#     if(left[node] != -1):
#       inOrder(key,left,right,left[node])
#     result_inOrder.append(key[node])
#     if key[node] == key[0]:
#       # print(result_inOrder)
#       key_index = len(result_inOrder)- 1
#       # print(key_index)
#       # print(result_inOrder.index(4))
#     if(right[node] != -1):
#       inOrder(key,left,right,right[node])
#   return(result_inOrder,key_index)

# def IsBinarySearchTree(key,left,right,node):
#   boolean = True
#   result ,myIndex= inOrder(key,left,right,node)
#   # print(result)
#   # print(result)
#   # print(myIndex)
#   for i in range(0,myIndex):
#     # print(myIndex)
#     if result[i] >= result[i+1]:
#       # print("left eror")
#       boolean =  False
#   for j in range(myIndex,len(result) -1):
#     # print(result[j+1])
#     if result[j] > result[j+1]:
#       boolean = False
#   return boolean
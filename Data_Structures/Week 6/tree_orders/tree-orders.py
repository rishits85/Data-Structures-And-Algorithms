# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
  def read(self):
    self.n = int(sys.stdin.readline())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    self.result_preorder = []
    self.result_inOrder = []
    self.result_postOrder = []
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c

  def inOrder(self,node):
    # Finish the implementation
    # You may need to add a new recursive method to do that
    if self.left[node] == -1 and self.right[node] == -1:
      self.result_inOrder.append(self.key[node])
      return
    else:
      if(self.left[node] != -1):
        self.inOrder(self.left[node])
      self.result_inOrder.append(self.key[node])
      if(self.right[node] != -1):
        self.inOrder(self.right[node])
    return(self.result_inOrder)

  def preOrder(self,node):
    # Finish the implementation
    # You may need to add a new recursive method to do that
    self.result_preorder.append(self.key[node])
    if self.left[node] == -1 and self.right[node] == -1:
      return
    else:
      if(self.left[node] != -1):
        self.preOrder(self.left[node])
      # xprint(self.result
      if(self.right[node] != -1):
        self.preOrder(self.right[node])
    return(self.result_preorder)
                
    return self.result

  def postOrder(self,node):
    # self.result = []
    if self.left[node] == -1 and self.right[node] == -1:
      self.result_postOrder.append(self.key[node])
      return
    else:
      if(self.left[node] != -1):
        self.postOrder(self.left[node])
      if(self.right[node] != -1):
        self.postOrder(self.right[node])
      self.result_postOrder.append(self.key[node])
    return(self.result_postOrder)
    

                
    return self.result

def main():
  tree = TreeOrders()
  tree.read()
  print(" ".join(str(x) for x in tree.inOrder(0)))
  print(" ".join(str(x) for x in tree.preOrder(0)))
  print(" ".join(str(x) for x in tree.postOrder(0)))

threading.Thread(target=main).start()

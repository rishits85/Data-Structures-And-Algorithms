# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeHeight:
        def read(self):
                self.n = int(sys.stdin.readline())
                self.parent = list(map(int, sys.stdin.readline().split()))

        def compute_height(self,sibling,numElements,height):
            sibling2 = []
            # height = 0
            if len(sibling) == 0:
                print("sibling length zero")
                for i in range(self.n):
                    if numElements == len(self.parent):
                        print("numElements size exceeded")
                        break
                    elem = self.parent[i]
                    if elem == -1:
                        numElements += 1
                        # print(numElements)
                        sibling2.append(self.parent.index(elem))
                        print (sibling2)
                        return self.compute_height(sibling2,numElements,height)
                    else:
                        continue
            else:
                print("sibling")
                for i in sibling:
                    for j in range(self.n):
                        if numElements == len(self.parent):
                            break
                        elem = self.parent[j]
                        if elem == i:
                            numElements +=1
                            # print(numElements)
                            print (sibling2)
                            sibling2.append(self.parent.index(elem))
                            return self.compute_height(sibling2,numElements,height)
                        else:
                            continue
            # height += 1
            # find the index of -1
            # check which other elements have that value
            # if they dont, 
            # if many of them do, check their index. Find if other elements have that index
                # counted = []
                # Replace this code with a faster implementation
                # print(self.n)
                # print(self.parent)
                # maxHeight = 0
                # for vertex in range(self.n):
                    # if vertex in self.parent:
                        # counted.append(vertex)
                        # maxHeight = len(counted) + 1
                        # height = 0
                        # i = vertex
                        # while i != -1:
                        #         height += 1
                        #         i = self.parent[i]
                        # maxHeight = max(maxHeight, height);
                # print (counted)
                height += 1
                return height;

def main():
  tree = TreeHeight()
  tree.read()
  sibling = []
  numElements = 0
  height = 0
  print(tree.compute_height(sibling,numElements,height))

threading.Thread(target=main).start()


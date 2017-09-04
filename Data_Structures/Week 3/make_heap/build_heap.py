# python3

import heapq
import random
# from profilestats import profile

class HeapBuilder:
  def __init__(self):
    self._swaps = []
    self._data = []
    self._n = 0

  def ReadData(self):
    self._n = int(input())
    self._data = [int(s) for s in input().split()]
    assert self._n == len(self._data)


  def WriteResponse(self):

    print(len(self._swaps))
    for swap in self._swaps:
      print(swap[0], swap[1])

  # @profile
  def GenerateSwaps(self):

    # The following naive implementation 2*i + 1ust sorts 
    # the given sequence using selection sort algorithm
    # and saves the resulting sequence of swaps.
    # This turns the given array into a heap, 
    # but in the worst case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation

    # n is parent index
    # print("n")
    # print(n)
    
    # parent = self._data[child_index]


    # This represesntation will not work as python has maximum recursion limit set to 1000. The depth will be exceeded with this. Put max values in stress-test.py and figure it out
    # if n < 0:
    #   return self._swaps
    # # [5 4 3 2 1]
    # if (2*n + 2) > self._n:
    #   return self.GenerateSwaps(n-1)
    # else:
    #   # print("n")
    #   # print(n)
    #   if (2*n + 2) == self._n:
    #     child_index = 2*n + 1
    #   else:
    #     child_index = self._data.index(min(self._data[(2*n) + 1],self._data[(2*n) + 2]))

    # if self._data[n] > self._data[child_index]:
    #   # print("child is smaller for n = " + str(n))
    #   # print(self._data)
    #   self._swaps.append((n, child_index))
    #   self._data[n], self._data[child_index] = self._data[child_index], self._data[n]
    #   n = child_index
    #   return self.GenerateSwaps(n)
    # else:
    #   return self.GenerateSwaps(n-1)


# monitor child instead of parent
    size=self._n
    for root in range((size//2)-1,-1,-1):
        root_val = self._data[root]             # save root value
        child = 2*root+1
        while(child<size):
            if child<size-1 and self._data[child]>self._data[child+1]:
                child+=1
            if root_val<=self._data[child]:     # compare against saved root value
                break
            self._data[(child-1)//2]=self._data[child]   # find child's parent's index correctly
            self._swaps.append(((child-1)//2,child))
            child=2*child+1
            # print(child)
        self._data[(child-1)//2]=root_val       # here too, and assign saved root value
    return self._data

    # for i in range(self._n//2 , -1, -1):
    #   # print("For loop")
    #   # print(i)
    #   child_index = 0
    #   if (2*i + 2) == self._n:
    #     child_index = 2*i + 1
    #   elif (2*i + 2) < self._n and :
    #     # child_index = self._data.index(min(self._data[(2*i) + 1],self._data[(2*i) + 2]))

    #   else:
    #     child_index = 0

      # while self._data[i] > self._data[child_index]:
      #   print("child is smaller for n = " + str(i))
      #   print(child_index)
      #   if child_index == 0:
      #     break
      #   else:
      #     self._swaps.append((i, child_index))
      #     self._data[i], self._data[child_index] = self._data[child_index], self._data[i]
      #     if child_index <= n//2:
      #       i = child_index
      #     else:
      #       break
      #     if (2*i + 2) == self._n:
      #       child_index = 2*i + 1
      #     elif(2*i + 2) < self._n:
      #       child_index = self._data.index(min(self._data[(2*i) + 1],self._data[(2*i) + 2]))
      #     else:
            

    #     print("hello work")
    #     self._data[i], self._data[child_index] = self._data[child_index], self._data[i]
    #     print(self._data)
      
    # for i in range(len(self._data)//2 , 0):
    #   print(i)
    #   if self._data[i] > self._data[2*i + 1]:
    #     self._swaps.append((i, 2*i + 1))
    #     self._data[i], self._data[2*i + 1] = self._data[2*i + 1], self._data[i]
    #   elif self._data[i] > self._data[2*i + 2]:
    #     self._swaps.append((i, 2*i + 2))
    #     self._data[i], self._data[2*i + 2] = self._data[2*i + 2], self._data[i]

  # def Compare(self):

  def Solve(self):
    self.ReadData()
    self.GenerateSwaps()
    self.WriteResponse()
    print(self._data)

if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.Solve()

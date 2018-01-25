# python3

import sys
import threading

sys.setrecursionlimit(10 ** 7)  # max depth of recursion
threading.stack_size(2 ** 25)  # new thread will get stack of such size


class TreeHeight:
   
    def __init__(self):
        self.n = 0
        self.parent = []
        self.cache = []

    def read(self):
        """Reads data from standard input."""
        self.n = int(sys.stdin.readline())
        self.parent = list(map(int, sys.stdin.readline().split()))
        self.cache = [0] * self.n
# algo can be explained as follows: 
# take a value between 0 and n. find the value of that index in the parent. take that value, and make it index. Find value of that. 
# continue this until you reach -1, where you return 1. 
# The above calls are recursive, as a result the addition happes every time you make the value index and find it's value. This problem could have been solved by going reverse. i.e 
# instead of beginning with the root and trying to find siblings, we begin at random element and try to find it's distance to root. 
# the key was node id here. Look for such keys that can help you design recursive algorithms. the reason it was the key is that it conects values and indexes
# nodeID was related to other indexes which would be chained together to form the recursion
# One way is to have an array of zeros. Keep appending shit to array of zeros and find what you need from it. This is done when individual arrays are concerned. Below are approaches
# begin from top and go to bottom
# begin from bottom and go to top. 
# do it for each element
    def path_len(self, node_id):
        """Returns path length from given node to the root."""
        parent = self.parent[node_id]
        print("parent")
        print(parent)
        print("node_id]")
        print(node_id)
        if parent == -1:
            print("parent -1")
            return 1

        if self.cache[node_id]:
            print("node in cache")
            return self.cache[node_id]


        self.cache[node_id] = 1 + self.path_len(self.parent[node_id])
        print(self.cache)
        return self.cache[node_id]

    def compute_height(self):
        """Computes the tree height."""
        return max([self.path_len(i) for i in range(self.n)])


def main():
    tree = TreeHeight()
    tree.read()
    print(tree.compute_height())


threading.Thread(target=main).start()

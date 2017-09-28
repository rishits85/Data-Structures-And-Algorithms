#Uses python3

import sys
import queue
import heapq
import random

def distance(adj, cost, s, t):
    #write your code here
    count = 0
    count2 = 0
    count3 = []
    dist = [sys.maxsize for i in range(n)]
    prev = [0 for i in range(n)]
    dist[s] = 0
    H = []
    # Make queue H with dist values as key
    # While H is not empty,
    while count < n:
        if count > 1 and count3[count-1] == count3[count - 2]:
            break
        count += 1
        for i in range(n):
            heapq.heappush(H,i) 
        while len(H)!= 0:
        # u = extractMin(H)
            index = -1
            u = heapq.heappop(H)
        # for all edges from u
            for i in adj[u]:
                index += 1
                # print(u)
                # print(i)
                # print(cost)
                # print(dist[i])
            # relax dist[v]
                # print(cost[u][index])
                if dist[i] > dist[u] + cost[u][index]:
                    dist[i] = dist[u] + cost[u][index]
                    prev[i] = u
                    count2 +=1
        count3.append(count2)
        # print(count3)
        # print(count)
                # heapq.heappush()
        # changpriority(H,v,dist[v])
    # print(dist)
    if dist[t] == sys.maxsize:
        return -1
    else:
        return dist[t]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    # data = []
    # data.append(1000)
    # data.append(100000)
    # for i in range(300000):
    #     data.append(random.randint(0,1000))
    # data.append(3)
    # data.append(4)
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    # print(data)
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    # print(edges)
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s, t = data[0] - 1, data[1] - 1
    # print(cost)
    # print(adj)
    print(distance(adj, cost, s, t))

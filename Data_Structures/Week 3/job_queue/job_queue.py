# # python3

# import heapq

# class JobQueue:
#     def read_data(self):
#         self.num_workers, m = map(int, input().split())
#         self.jobs = list(map(int, input().split()))
#         assert m == len(self.jobs)

#     def write_response(self):
#         for i in range(len(self.jobs)):
#           print(self.assigned_workers[i], self.start_times[i]) 

#     def sift_down(a, i):
#         l = 2 * i + 1
#         r = 2 * i + 2

#         m = i
#         if l < len(a) and ((a[l][0] < a[m][0]) or (a[l][0] == a[m][0] and a[l][1] < a[m][1])):
#             m = l

#         if r < len(a) and ((a[r][0] < a[m][0]) or (a[r][0] == a[m][0] and a[r][1] < a[m][1])):
#             m = r

#         if i != m:
#             a[i], a[m] = a[m], a[i]
#             JobQueue.sift_down(a, m)

#     def assign_jobs(self):
#         # TODO: replace this code with a faster algorithm. 
#         self.assigned_workers = [None] * len(self.jobs)
#         self.start_times = [None] * len(self.jobs)
#         next_free_time = [(0, i) for i in range(self.num_workers)]

#         for i in range(len(self.jobs)):
#           self.assigned_workers[i] = next_free_time[0][1]
#           self.start_times[i] = next_free_time[0][0]
#           # print(next_free_time)
#           next_free_time[0] = (next_free_time[0][0] + self.jobs[i], next_free_time[0][1])
#           JobQueue.sift_down(next_free_time, 0)

#     def solve(self):
#         self.read_data()
#         self.assign_jobs()
#         self.write_response()

# if __name__ == '__main__':
#     job_queue = JobQueue()
#     job_queue.solve()



# import heapq


class Worker:
    """Worker class.
    The workers are sorted by release time. If the release time is the same for
    both of them, workers are sorted by their thread_id.
    """

    def __init__(self, thread_id, release_time=0):
        self.thread_id = thread_id
        self.release_time = release_time

    # def __lt__(self, other):
    #     if self.release_time == other.release_time:
    #         return self.thread_id < other.thread_id
    #     return self.release_time < other.release_time

    # def __gt__(self, other):
    #     if self.release_time == other.release_time:
    #         return self.thread_id > other.thread_id
    #     return self.release_time > other.release_time


class JobQueue:

    def read_data(self):
        """Reads data from standard input."""
        self.num_workers, self.m = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        self.size = len(self.jobs)
        assert self.m == self.size

    def write_response(self):
        """Writes the response to standard output."""
        for i in range(len(self.jobs)):
          print(self.assigned_workers[i], self.start_times[i])

    def assign_jobs(self):
        """Assigns jobs to corresponding workers"""
        self.assigned_workers = []
        self.start_times = []
        self.result = []
        # self.worker_queue = [Worker(i) for i in range(self.num_workers)]
        # self.worker_queue_time = {i:Worker(i).release_time for i in range(self.num_workers)}
        self.worker_queue_time = [0 for i in range(self.num_workers)]
        self.worker_id = [i for i in range(self.num_workers)]
        print(self.worker_id)

        for job in range(self.m):
            self.assigned_workers.append(self.worker_id[0])
            self.start_times.append(self.worker_queue_time[0])
            self.worker_queue_time[0] += self.jobs[job]
            # print(self.jobs[job])
            # print(job)
            self.build_heap(self.worker_queue_time, self.worker_id)


    def solve(self):
        self.read_data()
        self.assign_jobs()
        self.write_response()

    def build_heap(self,data,index):
        size=len(data)
        print(size)
        for root in range((size//2)-1,-1,-1):
            root_val = data[root]             # save root value
            root_index = index[root]
            child = 2*root+1
            while(child<size):
                print(root)
                if child<size-1 and (data[child]>data[child+1]):
                    child+=1
                if root_val<=data[child]:     # compare against saved root value
                    break
                data[(child-1)//2]=data[child]   # find child's parent's index correctly
                index[(child-1)//2] = index[child]
                # self._swaps.append(((child-1)//2,child))
                child=2*child+1
                # print(child)
            data[(child-1)//2]=root_val       # here too, and assign saved root value
            index[(child-1)//2]= root_index
            print(data)
            print(index)
        return data


if __name__ == "__main__":
    job_queue = JobQueue()
    job_queue.solve()
# Time is an object. It will have an id. It should return an id
# use a hash

# python3

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    array_length = 10**7
    result = []
    contacts = [None]*array_length
    for cur_query in queries:
        if cur_query.number >= array_length:
            continue
        if cur_query.type == 'add':
            contacts[cur_query.number] = cur_query.name
        elif cur_query.type == 'del':
            contacts[cur_query.number] = None
        else:
            response = 'not found'
            if contacts[cur_query.number] != None:
                response = contacts[cur_query.number]
            result.append(response)

    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))

# class MyNum(object):
#     """docstring for MyNum"""
#     def __init__(self, num, someHash,name):
#         super(MyNum, self).__init__()
#         self.number = num 
#         self.hash = someHash
#         self.name = name
        
# class Query:
#     def __init__(self, query):
#         self.type = query[0]
#         self.number = int(query[1])
#         if self.type == 'add':
#             self.name = query[2]

# def read_queries():
#     n = int(input())
#     return [Query(input().split()) for i in range(n)]

# def write_responses(result):
#     print('\n'.join(result))

# def process_queries(queries):
#     result = []
#     # Keep list of all existing (i.e. not deleted yet) contacts.
#     # contacts = []
#     # choose p
#     p = 10000019
#     # choose a and b
#     a = 34
#     b = 2
#     # choose m
#     m = 1000
#     contacts = [[]]*m
#     # print(contacts)
#     for cur_query in queries:
#         myHash = ((a*cur_query.number + b)%p)%m
#         # print(myHash)
#         if cur_query.type == 'add':
#                 thisNum = MyNum(cur_query.number,myHash,cur_query.name)
#                 contacts[myHash].append(thisNum)
#         elif cur_query.type == 'del':
#             response_obj = contacts[myHash]
#             i = len(response_obj) - 1
#             while(i >= 0):
#                 if response_obj[i].number == cur_query.number:
#                     # print(response_obj[i])
#                     response_obj.pop(i)
#                     # print(response)
#                 i -= 1
#         else:
#             response = 'not found'
#             if contacts[myHash] != 0:
#                 response_obj = contacts[myHash]
#                 for i in range (len(response_obj)):
#                     if response_obj[i].number == cur_query.number:
#                         response = response_obj[i].name
#                         # print(response)
#                     else:
#                         continue
#             else:
#                 response = "not found"
#             result.append(response)
#     return result

# if __name__ == '__main__':
#     write_responses(process_queries(read_queries()))


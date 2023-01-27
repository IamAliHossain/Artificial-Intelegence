from cgi import print_directory
from random import vonmisesvariate


# total_vertex = int(input("Enter num of vertex: "))
graph = {'A':['C', 'B'], 'B' :['E', 'D'], 'C':['F'], 'D':[], 'E':['F'], 'F':[]}
ok = True

stack = []
visited = []

def DFS(graph, temp) :
    visited.append(temp)
    stack.append(temp)

    while stack :
        node = stack.pop()
        print(node, end=" ")

        for child in graph[node] :
            if child not in visited :
                stack.append(child)
                visited.append(child)




    print(graph)

DFS(graph, 'A')







































# total_vertex = int(input("Enter num of vertex: "))
# graph = {}
# ok = True 
# visited = []
# queue = []

# def BFS(graph, temp) :
#     visited.append(temp)
#     queue.append(temp)

#     while queue :
#         node = queue.pop(0)
#         print(node, end=' ')

#         for child in graph[node] :
#             if child not in visited :
#                 queue.append(child)
#                 visited.append(child)
            

# for i in range(total_vertex):
#     vertex = input("Enter Vertex: ")
#     graph[vertex] = list()

#     while ok :
#         child = input(f'Enter the vertext {vertex} (-1 for exit) : ')
#         if child != -1 :
#             graph.append(child)
#         else :
#             ok = False 
#     ok = True

#     print(graph)

# BFS(graph, 'A')


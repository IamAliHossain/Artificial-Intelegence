# from configparser import RawConfigParser









graph = {'A':['B', 'C'], 'B' :['D', 'E'], 'C':['F'], 'D':[], 'E':['F'], 'F':[]}
ok = True
visited = []
queue = []
def BFS(graph, temp):
    queue.append(temp)
    visited.append(temp)

    while queue:
        node = queue.pop(0)
        print(node, end=' ')

        for child in graph[node] :
            if child not in visited :
                visited.append(child)
                queue.append(child)


    print(graph)

BFS(graph, 'A')







# 1-->3 5
# 2-->3 6
# 3-->4 6
# 4-->6
# 5-->6
# 6--blank
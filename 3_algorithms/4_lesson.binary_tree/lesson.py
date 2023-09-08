# # graph = {
# # 'A':['B','C'],
# # 'B':['D','E'],
# # 'C':['F'],
# # 'D':[],
# # 'E':['F'],
# # 'F':[]
# # }

# v_lst =[]
# queue = []
# def bfs(v_lst,graph,node):
#     v_lst.append(node)
#     queue.append(node)

#     while queue:
#         s = queue.pop(0)
#         print(s,end=' ')

#     for i in graph[s]:
#         if i not in v_lst:
#             v_lst.append(i)
#             queue.append(i)
    
# # bfs(v_lst, graph, 'D')

def dfs(graph,node,v_lst= None):
    if v_lst is None:
        v_lst = set()
        v_lst.add(node)
        print(node)

        for i in graph[node] - v_lst:
            dfs(graph, node,v_lst)
        return v_lst


graph = {
'0':set(['1','2']),
'1':set(['0','3','4']),
'2':set(['0']),
'3':set(['1','2']),
'4':set(['1','2','3']),
}
print(dfs(graph, '2'))

# denominations = [1, 2, 5, 10, 20, 50, 100]

# def returnChange(change, denominations):
#     toGiveBack = [0] * len(denominations)

#     for pos, coin in enumerate(reversed(denominations)):
#         while coin <= change:
#             change = change - coin
#             toGiveBack[pos] += 1
#     return(toGiveBack)

# print(returnChange(60, denominations))


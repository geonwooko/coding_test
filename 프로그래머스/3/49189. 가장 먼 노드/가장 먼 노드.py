from heapq import heappop, heappush

def solution(n, edge):
    answer = 0
    adj_list = {i:[] for i in range(n)}
    for e in edge:
        adj_list[e[0]-1].append(e[1]-1)
        adj_list[e[1]-1].append(e[0]-1)
    res = dijkstra(adj_list, 0)
    return sum([i==max(res) for i in res])

def dijkstra(graph, start, end=None):
    n = len(graph)
    
    heap = [(start, 0)]
    seen = set()
    d = [float('inf')] * n
    d[start] = 0
    while heap:
        curr, dist = heappop(heap)
        # if curr in seen:
        #     continue
        if dist > d[curr]: 
            continue 
        # seen.add(curr)
        for child in graph[curr]:
            if d[child] > dist + 1:
                d[child] = dist + 1
                heappush(heap, (child, dist+1))
                
    return d
from collections import defaultdict
import heapq
def solution(n, start, end, roads, traps):
    answer = 0
    graph = defaultdict(list)
    for p, q, s in roads:
        graph[p].append((q, s))
    
    Q = [(0, start)]
    dis = defaultdict(int)

    while Q:
        time, p = heapq.heappop(Q)
        if p in traps:
            for i, v in enumerate(graph[p]):
                if v[1] == s:
                    del graph[p][i]
                
                    


    return answer
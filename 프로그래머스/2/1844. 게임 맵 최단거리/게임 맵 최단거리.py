from collections import deque
def solution(maps):
    answer = 0
    n,m = len(maps), len(maps[0])
    d = deque([[0,0, 1]])
    visited = [[False]* m for i in range(n)]
    visited[0][0]= True
    while d:
        x,y, l = d.popleft()
        
        visited[x][y] = True
        if y<m-1 and not visited[x][y+1] and maps[x][y+1]:
            d.appendleft([x, y+1, l+1])
        if x<n-1 and not visited[x+1][y] and maps[x+1][y]:
            d.appendleft([x+1, y, l+1])
        if x>0 and not visited[x-1][y] and maps[x-1][y]:
            d.append([x-1, y, l+1])
        if y>0 and not visited[x][y-1] and maps[x][y-1]:
            d.append([x, y-1, l+1])
        if x == n-1 and y == m-1:
            return l
        
    return -1
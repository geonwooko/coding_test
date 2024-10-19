from collections import deque

def solution(maps):
    
    n,m = len(maps), len(maps[0])
    sx, ex, lx = None, None, None
    for i in range(n):
        for j in range(m):
            if maps[i][j] == "S":
                sx, sy = i,j
            elif maps[i][j] == 'E':
                ex, ey = i,j
            elif maps[i][j] == 'L':
                lx, ly = i,j
        if sx is not None and ex is not None and lx is not None:
            break
    
    d = deque([(sx, sy, 0)])
    visited = [[False]*m for i in range(n)]
    answer = 0
    while d:
        x,y, l = d.popleft()
        visited[x][y] = True
        xflag, yflag = x>sx, y>sy

        if y<m-1 and not visited[x][y+1] and maps[x][y+1]!='X':
            if yflag:
                d.appendleft([x, y+1, l+1])
            else:
                d.append([x, y+1, l+1])
        if x<n-1 and not visited[x+1][y] and maps[x+1][y]!='X':
            if xflag:
                d.appendleft([x+1, y, l+1])
            else:
                d.append([x+1, y, l+1])
        if x>0 and not visited[x-1][y] and maps[x-1][y]!='X':
            if xflag:
                d.append([x-1, y, l+1])
            else:
                d.appendleft([x-1, y, l+1])
        if y>0 and not visited[x][y-1] and maps[x][y-1]!='X':
            if yflag:
                d.append([x, y-1, l+1])
            else:
                d.appendleft([x, y-1, l+1])
        if x == lx and y == ly:
            answer+=l
            break
    if answer == 0:
        return -1
    print(answer)
    d = deque([(lx, ly, 0)])
    visited = [[False]*m for i in range(n)]
    
    while d:
        x,y, l = d.popleft()
        visited[x][y] = True
        xflag, yflag = x>lx, y>lx
        if y<m-1 and not visited[x][y+1] and maps[x][y+1]!='X':
            if yflag:
                d.appendleft([x, y+1, l+1])
            else:
                d.append([x, y+1, l+1])
        if x<n-1 and not visited[x+1][y] and maps[x+1][y]!='X':
            if xflag:
                d.appendleft([x+1, y, l+1])
            else:
                d.append([x+1, y, l+1])
        if x>0 and not visited[x-1][y] and maps[x-1][y]!='X':
            if xflag:
                d.append([x-1, y, l+1])
            else:
                d.appendleft([x-1, y, l+1])
        if y>0 and not visited[x][y-1] and maps[x][y-1]!='X':
            if yflag:
                d.append([x, y-1, l+1])
            else:
                d.appendleft([x, y-1, l+1])
        if x == ex and y == ey:
            return answer + l
    return -1
                

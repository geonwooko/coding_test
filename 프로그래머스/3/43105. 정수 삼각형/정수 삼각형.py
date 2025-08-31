def solution(triangle):
    n = len(triangle)
    trace = [[0 for j in range(i+1)] for i in range(n)]
    for i in range(n):
        for j in range(i+1):
            if i == j == 0:
                trace[i][j] = triangle[i][j]
                continue 
            
            upper = trace[i-1][j] if j < i else 0 
            upper_left = trace[i-1][j-1] if j > 0 else 0
            trace[i][j] = max(upper, upper_left) + triangle[i][j]
    return max(trace[-1])
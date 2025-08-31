def solution(m, n, puddles):
    answer = 0
    fasted = [[[10**9, 0] for j in range(m)] for i in range(n)] 
    fasted[0][0] = [0, 1]
    for i in range(0, n):
        for j in range(0, m):
            if [j+1, i+1] in puddles or i == j == 0:
                continue
            left = fasted[i-1][j][0] if i > 0 else 10**9
            down = fasted[i][j-1][0] if j > 0 else 10**9
            left_path = fasted[i-1][j][1]
            down_path = fasted[i][j-1][1]

            if left == down:
                all_path = left_path + down_path
            elif left < down:
                all_path = left_path
            else:
                all_path = down_path
            
            if fasted[i][j][0] > min(left+1, down+1):
                fasted[i][j][0] = min(left+1, down+1)
                fasted[i][j][1] = all_path
                # print('reset', fasted[0][2])
            elif fasted[i][j][0] == min(left+1, down+1):
                fasted[i][j][1] += all_path
                # print("add")
                # print(i, j, all_path, fasted[i][j][0])
            print(i, j,fasted[i][j][0], fasted[i][j][1])
    return fasted[n-1][m-1][1] % 1000000007
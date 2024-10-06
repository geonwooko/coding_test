from math import log
def solution(arr):
    answer = [0,0]
    cur = arr
    n =int(log(len(arr),2))
    for block in range(1, n+1):
        new_arr = [[None]*(len(arr)//(2**block)) for i in range(len(arr)//(2**block))]
        for i in range(0, len(new_arr)):
            for j in range(0, len(new_arr)):
                if cur[i*2][j*2] == cur[i*2][j*2+1] == cur[i*2+1][j*2] == cur[i*2+1][j*2+1]:
                    new_arr[i][j] = cur[i*2][j*2]
                else:
                    if cur[i*2][j*2] is not None: answer[cur[i*2][j*2]] += 1
                    if cur[i*2][j*2+1] is not None: answer[cur[i*2][j*2+1]] += 1
                    if cur[i*2+1][j*2] is not None: answer[cur[i*2+1][j*2]] += 1
                    if cur[i*2+1][j*2+1] is not None: answer[cur[i*2+1][j*2+1]] += 1
        cur = new_arr
    if cur[0][0] is not None:
        answer[cur[0][0]] += 1
    return answer
    
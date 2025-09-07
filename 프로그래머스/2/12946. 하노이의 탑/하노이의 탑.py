def solution(n):
    return hanoi(n, 1, 2, 3, [])

def hanoi(n, start, via, to, res):
    if n == 1:
        return res + [[start, to]]
    else:
        res = hanoi(n-1, start, to, via, res)
        res += [[start, to]]
        return hanoi(n-1, via, start, to, res)

def solution(x):
    numsum = sum([int(s) for s in str(x)])
    if x % numsum == 0:
        return True
    else:
        return False
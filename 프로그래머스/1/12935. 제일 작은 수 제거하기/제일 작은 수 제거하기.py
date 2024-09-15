def solution(arr):
    if len(arr) == 1:
        return [-1]
    else:
        minnum = min(arr)
        return [num for num in arr if not minnum==num]
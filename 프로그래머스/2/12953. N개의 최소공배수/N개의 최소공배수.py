def solution(arr):
    while len(arr) >= 2:
        a,b = arr[0], arr[1]
        del arr[:2]
        arr.append(lcm(a,b))
    return arr[0]

def bcd(a,b):
    if b%a == 0:
        return a
    else:
        return bcd(b%a, a)
    
def lcm(a,b):
    return a*b // bcd(a,b)
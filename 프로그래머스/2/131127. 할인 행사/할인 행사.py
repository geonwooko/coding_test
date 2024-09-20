from collections import Counter

def solution(want, number, discount):
    count = Counter(discount[:10])
    answer = 1 if check(want, number, count) else 0
    for i in range(1, len(discount)-10+1):
        
        count[discount[i-1]] -= 1
        count[discount[i+9]] += 1
        if check(want, number, count):
            answer += 1
    return answer

def check(want, number, count):
    for w,n in zip(want,number):
        if not count.get(w, 0) >= n:
            return False
    return True
        
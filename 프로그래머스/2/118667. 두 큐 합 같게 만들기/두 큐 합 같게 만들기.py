from collections import deque
def solution(queue1, queue2):
    que1_sum, que2_sum = sum(queue1), sum(queue2)
    all_sum = que1_sum + que2_sum
    que1 = deque(queue1)
    que2 = deque(queue2)
    answer = 0
    n = (len(queue1) + len(queue2)) * 2
    while que1_sum != que2_sum:
        if que1_sum > que2_sum:
            f = que1.popleft()
            que2_sum += f
            que1_sum -= f
            que2.append(f)
        else:
            f = que2.popleft()
            que1_sum += f
            que2_sum -= f
            que1.append(f)
        answer += 1
        
        if answer > n:
            return -1
    return answer
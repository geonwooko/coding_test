from collections import deque
def solution(number, k):
    num_del = 0
    stack = deque()
    numbers = deque(list(number))
    while k > num_del and numbers:
        cur = numbers.popleft()
        while stack and stack[-1] < cur and k > num_del:
            stack.pop()
            num_del += 1
        stack.append(cur)
        
    return "".join((list(stack)+list(numbers))[:len(number)-k])
        
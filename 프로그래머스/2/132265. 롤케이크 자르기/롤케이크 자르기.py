from collections import deque, Counter
def solution(s):
    left_counter = dict(Counter(s))
    dq = deque(s)
    res = 0
    right_set = set()
    for i in range(len(s)):
        el = dq.pop()
        right_set.add(el)
        left_counter[el] -= 1
        if left_counter[el] == 0:
            del left_counter[el]
        res += int(len(left_counter) == len(right_set))
    return res
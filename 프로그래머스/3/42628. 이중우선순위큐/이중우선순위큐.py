from heapq import heapify, heappush, heappop
def solution(operations):
    minheap = []
    maxheap = []
    for op in operations:
        o, num = op.split(" ")
        if o == 'I':
            heappush(minheap, int(num))
            heappush(maxheap, -int(num))
        elif num == '1' and minheap:
            el = -heappop(maxheap)
            del minheap[minheap.index(el)]
        elif minheap:
            el = -heappop(minheap)
            del maxheap[maxheap.index(el)]
    if not maxheap: return [0, 0]
    return max(minheap), min(minheap)
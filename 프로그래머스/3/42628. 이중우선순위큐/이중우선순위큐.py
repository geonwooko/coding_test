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
            del minheap[len(minheap) - minheap[::-1].index(el) - 1]
        elif minheap:
            el = -heappop(minheap)
            del maxheap[len(maxheap) - maxheap[::-1].index(el) - 1]
    if not maxheap: return [0, 0]
    return max(minheap), min(minheap)
def solution(elements):
    answer = 0
    lst = set()
    k = len(elements)
    length = 1
    chk_element = elements + elements

    for j in range(0,k):
        for i in range(0,k): 
            lst.add(sum(chk_element[i:i+length]))
        length += 1

    return len(lst)
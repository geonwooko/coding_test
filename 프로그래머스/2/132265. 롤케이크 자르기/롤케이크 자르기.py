from collections import Counter
def solution(topping):
    hyung, dongsang = dict(), Counter(topping)
    answer = 0
    for i in range(len(topping)):
        cur_top = topping[i]
        hyung[cur_top] = hyung.get(cur_top, 0) + 1
        if dongsang[cur_top] == 1:
            del dongsang[cur_top]
        else:
            dongsang[cur_top] -= 1
        if len(hyung) == len(dongsang):
            answer += 1
    return answer
    
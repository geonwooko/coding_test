def solution(num):
    count = 0
    while True:
        if count >= 500:
            return -1
        elif num % 2 ==0:
            num /= 2
        elif num == 1:
            return count
        
        else:
            num = 3*num+1
        count += 1
def solution(s):
    answer = True
    
    num_p = 0
    num_y = 0
    for string in s:
        if string.upper() == 'Y':
            num_y += 1
        elif string.upper() == 'P':
            num_p += 1

    return num_p == num_y
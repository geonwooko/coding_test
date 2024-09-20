def solution(s):
    doudle_s = s+s
    answer = 0
    for i in range(len(s)):
        if check(doudle_s[i:len(s)+i]):
    
            answer+= 1
    return answer

def check(s):
    stack = []
    for i in s:
        if not stack:
            stack.append(i)
        elif i == ")" and stack[-1] == '(':
            stack.pop(-1)
        elif i == "]" and stack[-1] == "[":
            stack.pop(-1)
        elif i == "}" and stack[-1] == "{":
            stack.pop(-1)
        else:
            stack.append(i)
    
    return not stack
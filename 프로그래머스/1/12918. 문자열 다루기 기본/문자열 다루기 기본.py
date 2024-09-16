def solution(s):
    try:
        int(s)
        if len(s) in [4,6]:
            return True
        else:
            return False
    except:
        return False
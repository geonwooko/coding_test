def convert(m):
    return int(m[0])*60 + int(m[1])
def solution(book_time):
    book_time = sorted([(convert(s.split(":")), convert(e.split(":")))  for s,e in book_time])
    rooms = [[]]
    for start, end in book_time:
        
        for i in range(len(rooms)):
            if rooms[i] and rooms[i][0]+10 <= start:
                del rooms[i][0]
        if all(rooms):
            rooms.append([])
        for i in range(len(rooms)):
            if not rooms[i]:
                rooms[i].append(end)
                break
    return len(rooms)
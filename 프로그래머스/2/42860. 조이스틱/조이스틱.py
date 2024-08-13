def solution(name):
    answer = 0
    alp_dict = {chr(i):min(i-ord('A'),ord('Z')-i+1) for i in range(ord('A'),ord('Z')+1)}
    moving = len(name) -1
    for i in range(len(name)):
        answer += alp_dict[name[i]]
        go = i + 1
        while go < len(name) and name[go] == 'A':
            go += 1
        moving = min(moving, i*2+len(name)-go,(len(name)-go)*2 + i)
    answer += moving
    
    return answer
def solution(citations):
    citations.sort(reverse=True)
    for i in range(len(citations)):
        if citations[i] < i+1:
            print(i+1)
            print(citations[i])
            return i
    return len(citations)

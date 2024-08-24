import heapq
def solution(jobs):
    answer = 0
    # jobs.sort(key = lambda x: (x[0],x[1]))
    start = -1
    now = 0
    heap = []
    done = 0
    while done < len(jobs):
        for job in jobs:
            if start < job[0] <= now:
                heapq.heappush(heap,(job[1],job[0]))
        if heap:
            job = heapq.heappop(heap)
            start = now
            now += job[0]
            done += 1
            answer += now - job[1]
        else:
            now += 1
    return answer//len(jobs)
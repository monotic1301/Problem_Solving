def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    rocks.append(distance)
    left, right = 1,distance
    while left <= right:
        mid = (left + right)//2
        prev = 0
        removed = 0
        for rock in rocks:
            if rock-prev < mid:
                removed += 1
                if removed > n:
                    break
            else:
                 prev = rock
        
        if removed > n:
            right = mid - 1
        else:
            answer = mid
            left = mid + 1
    return answer
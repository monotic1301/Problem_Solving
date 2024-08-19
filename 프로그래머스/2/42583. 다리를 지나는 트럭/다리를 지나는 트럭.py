from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    trucks = deque(truck_weights)
    bridge = deque([0] * bridge_length)
    sum_bridge = 0
    while trucks:
        answer += 1
        b = bridge.pop()
        sum_bridge -= b
        if sum_bridge + trucks[0] <= weight:
            truck = trucks.popleft()
            sum_bridge += truck
            bridge.appendleft(truck)
        else:
            bridge.appendleft(0)
    answer += bridge_length
    
    return answer
import sys

n, d, k, c = map(int,sys.stdin.readline().split())
food = []
for i in range(n):
    food.append(int(sys.stdin.readline()))

max_dish = 0
window = [food[i] for i in range(-k,0)]
for j in range(n):
    del window[0]
    window.append(food[j])
    temp = set(window)
    temp.add(c)
    if len(temp) > max_dish:
        max_dish = len(temp)
print(max_dish)
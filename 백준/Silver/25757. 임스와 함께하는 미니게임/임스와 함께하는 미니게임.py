import sys

N, game = sys.stdin.readline().strip().split()
N = int(N)
people = set([])
for _ in range(N):
    people.add(sys.stdin.readline().strip())
if game == "Y":
    print(len(people)//1)
elif game == "F":
    print(len(people)//2)
elif game == "O":
    print(len(people)//3)

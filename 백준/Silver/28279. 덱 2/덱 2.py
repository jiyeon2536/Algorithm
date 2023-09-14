# 덱2
from collections import deque
import sys
n = int(sys.stdin.readline().strip())
q = deque()
for i in range(n):
    command = list(map(int, sys.stdin.readline().strip().split()))
    if command[0] == 1:
        q.appendleft(command[1])
    elif command[0] == 2:
        q.append(command[1])
    elif command[0] == 3:
        if q:
            tmp = q.popleft()
            print(tmp)
        else:
            print(-1)
    elif command[0] == 4:
        if q:
            tmp = q.pop()
            print(tmp)
        else:
            print(-1)
    elif command[0] == 5:
        print(len(q))
    elif command[0] == 6:
        if q:
            print(0)
        else:
            print(1)
    elif command[0] == 7:
        if q:
            print(q[0])
        else:
            print(-1)
    elif command[0] == 8:
        if q:
            print(q[-1])
        else:
            print(-1)
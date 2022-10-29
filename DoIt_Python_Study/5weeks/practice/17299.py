from collections import Counter
from sys import stdin

n = int(stdin.readline())
nums = list(map(int, stdin.readline().split()))

nums_count = Counter(nums)

answer = [-1] * n
stack = []

for i in range(n):
    while stack and nums_count[nums[stack[-1]]] < nums_count[nums[i]]:
        answer[stack.pop()] = nums[i]
    stack.append(i)

print(*answer)
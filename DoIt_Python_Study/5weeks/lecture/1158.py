N, K = map(int,input().split())

nums = list(range(1,N+1))
index = K-1
answer = []

while True:

    answer.append(str(nums[index]))
    nums = nums[:index]+nums[index+1:]

    if not nums:
        break

    index = (index+K-1)%len(nums)

print("<"+", ".join(answer)+">")


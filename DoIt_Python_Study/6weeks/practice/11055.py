n=int(input())
array=list(map(int, input().split()))

d=[1]*n
d[0]=array[0]
for i in range(1,n):
  for j in range(i):
    if array[j]<array[i]:
      d[i]=max(d[i], d[j]+array[i])
    else:
      d[i]=max(d[i], array[i])

print(max(d))

# 참고 : https://velog.io/@bye9/%EB%B0%B1%EC%A4%80%ED%8C%8C%EC%9D%B4%EC%8D%AC-11055-%EA%B0%80%EC%9E%A5-%ED%81%B0-%EC%A6%9D%EA%B0%80-%EB%B6%80%EB%B6%84-%EC%88%98%EC%97%B4
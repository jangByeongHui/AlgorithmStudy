import sys

num = sys.stdin.readline()
num=int(num)

fac=1

for i in range(2,num+1):
    fac*=i

fac=str(fac)
count=0
for i in range(len(fac)-1,0,-1):
    if fac[i] in '0':
        count+=1
    else:
        break
print(count)
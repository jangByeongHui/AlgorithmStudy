import sys

Target = sys.stdin.readline().rstrip()
Target_int =int(Target)
Target_len=len(Target)
broken_num=int(sys.stdin.readline())
Min = Target_int
Min_Value=0
Min_count=0

if broken_num!=0:
    broken_Buttons=list(map(int,sys.stdin.readline().rstrip().split()))
else:
    broken_Buttons = []

available_buttons=[i for i in range(9,-1,-1)]
now_ch = 100

for removeValue in broken_Buttons:
    if removeValue == '0':
        continue
    available_buttons.remove(removeValue)

def dfs(N, num, Target_len):
    global Min, Min_count,available_buttons,Min_Value
    if N == Target_len:
        if Min > abs(int(num)-Target_int):
            Min_Value=int(num)
            Min = abs(int(num) - Target_int)
            if Min_Value==0:
                Min_count=0
            else:
                Min_count=len(str(Min_Value))
        return
    else:
        for button in available_buttons:
            dfs(N+1,num+str(button),Target_len)


if Target_int == now_ch:
    print(0)

elif abs(now_ch-Target_int)<=len(Target):
    print(abs(now_ch-Target_int))

else:
    count = 0
    if Target_len<2:
        dfs(0, "", Target_len+1)
    else:
        dfs(0,"",Target_len)

    print(Min_count+abs(Min_Value-Target_int))












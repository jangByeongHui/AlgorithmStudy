import sys

Target = sys.stdin.readline().rstrip()
Target_int =int(Target)
Target_len=len(Target)
broken_num=int(sys.stdin.readline())
Min = 99999999
Min_Value=0
Min_count=99999999

if broken_num!=0:
    broken_Buttons=list(map(int,sys.stdin.readline().rstrip().split()))
else:
    broken_Buttons = []

available_buttons=[i for i in range(10)]
now_ch = 100

for removeValue in broken_Buttons:
    available_buttons.remove(removeValue)

available_buttons.sort()

def dfs(N, num, Target_len):
    global Min, Min_count,available_buttons,Min_Value
    #print(num)
    if N == Target_len+1:
        # print("??", int(num))
        if Min == abs(int(num)-Target_int) and Min_count>len(str(int(num))):
            Min_Value=int(num)
            Min=abs(int(num)-Target_int)
            Min_count=len(str(Min_Value))
        if Min > abs(int(num)-Target_int):
                Min_Value=int(num)
                Min = abs(int(num) - Target_int)
                Min_count=len(str(Min_Value))
        return
    else:
        try:
            # print("?",int(num))
            if Min == abs(int(num) - Target_int) and Min_count > len(str(int(num))):
                Min_Value = int(num)
                Min = abs(int(num) - Target_int)
                Min_count = len(str(Min_Value))
            if Min > abs(int(num)-Target_int):
                Min_Value=int(num)
                Min = abs(int(num) - Target_int)
                Min_count=len(str(Min_Value))
        except:
            pass
        for button in available_buttons:
            dfs(N+1,num+str(button),Target_len)


if Target_int == now_ch:
    print(0)

elif broken_num == 10:
    print(abs(Target_int-now_ch))

else:
    dfs(-1,"",Target_len)
    # print(f'Min_count : {Min_count} Min_Value : {Min_Value} Targe_int : {Target_int}')
    print("found", Min_Value)
    print(min(Min_count+abs(Min_Value-Target_int),abs(now_ch-Target_int)))
import sys

Target = sys.stdin.readline().rstrip()
Target_int =int(Target)
broken_num=int(sys.stdin.readline())

if broken_num!=0:
    broken_Buttons=list(map(int,sys.stdin.readline().rstrip().split()))
else:
    broken_Buttons = []


available_buttons=[i for i in range(9,-1,-1)]
now_ch = 100

for removeValue in broken_Buttons:
    available_buttons.remove(removeValue)

if Target_int == now_ch:
    print(0)
elif abs(now_ch-Target_int)<=len(Target):
    print(abs(now_ch-Target_int))
else:
    count = 0
    cal_value=""
    for i in range(len(Target)):
        Min=9
        Max=-1
        MinMax_str="9"
        for available_button in available_buttons:
            if i==0 and abs(int(Target[i]) - available_button)<Min:
                Min = abs(int(Target[i]) - available_button)
                MinMax_str=str(available_button)
            elif i!=0 and int(Target[0]) in available_buttons and abs(int(Target[i]) - available_button)<Min:
                Min = abs(int(Target[i]) - available_button)
                MinMax_str = str(available_button)
            elif i!=0 and int(Target[0]) not in available_buttons and abs(int(Target[i]) - available_button)>Max:
                Max = abs(int(Target[i]) - available_button)
                MinMax_str = str(available_button)
        cal_value += MinMax_str
        count += 1
    count += abs(int(cal_value)-Target_int)

    print(count)




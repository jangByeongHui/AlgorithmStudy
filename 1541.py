import sys

Input =sys.stdin.readline()
Temp_Input=[]
Output=[]
init_pos=0

for i in range(len(Input)):

    if Input[i] == '+':
        Temp_Input.append(int(Input[init_pos:i]))
        Temp_Input.append("+")
        init_pos=i+1
    elif Input[i]=='-':
        Temp_Input.append(int(Input[init_pos:i]))
        Temp_Input.append("-")
        init_pos=i+1
else:
    Temp_Input.append(int(Input[init_pos:len(Input)]))

while '+' in Temp_Input:
    temp_list=[]
    init_pos=0

    while init_pos<len(Temp_Input):
        if Temp_Input[init_pos] == '+':
            result=Temp_Input[init_pos-1]+Temp_Input[init_pos+1]
            Temp_Input[init_pos+1]=result
            temp_list[-1]=result
            init_pos +=2
        else:
            temp_list.append(Temp_Input[init_pos])
            init_pos += 1
    Temp_Input=temp_list

ans=Temp_Input[0]
for i in range(1,len(Temp_Input)):
    if Temp_Input[i] != '-':
        ans -= Temp_Input[i]

print(ans)

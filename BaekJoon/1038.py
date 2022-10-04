from itertools import combinations

numbers = ["9","8","7","6","5","4","3","2","1","0"]
decrease_numbers = []

for i in range(1,11):
    for new_number in combinations(numbers,i):
        decrease_numbers.append(int("".join(new_number)))

decrease_numbers.sort()

N = int(input())

try:
    print(decrease_numbers[N])
except:
    print(-1)

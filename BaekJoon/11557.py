from collections import defaultdict
T = int(input())

for _ in range(T):
    N = int(input())
    school = defaultdict(int)

    for c in range(N):
        school_name, alcohol = input().split()

        school[school_name] += int(alcohol)
    max_school_name = ""
    max_alchol = -1

    for name, alc in school.items():
        if max_alchol < alc:
            max_school_name = name
            max_alchol = alc
    print(max_school_name)
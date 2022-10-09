while True:
    number = int(input())

    if number == -1:
        break
    candidates = []
    for i in range(1,number):
        if number % i == 0:
            candidates.append(i)

    if number == sum(candidates):
        print(f"{number} = ",end="")
        print(*candidates,sep=" + ")
    else:
        print(f"{number} is NOT perfect.")

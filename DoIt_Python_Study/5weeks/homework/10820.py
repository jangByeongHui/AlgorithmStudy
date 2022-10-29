
while True:
    try:
        text = input()

        up, lo, sp, nu = 0, 0, 0, 0

        for l in text:
            if l.isupper():
                up += 1
            elif l.islower():
                lo += 1
            elif l.isdigit():
                nu += 1
            elif l.isspace():
                sp += 1
        print(f"{lo} {up} {nu} {sp}")
    except EOFError:
        break



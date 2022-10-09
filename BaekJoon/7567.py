dishes = input()

height = 5

if len(dishes) > 0:
    prev_dish = dishes[0]
    height += 5

    for dish in dishes[1:]:

        if prev_dish == dish:
            height += 5
            prev_dish = dish
        else:
            height += 10
            prev_dish = dish
print(height)
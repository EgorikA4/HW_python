max_n = count = 0  # макс. число и его кол-во
while (n := int(input())) != 0:
    # если нашли новый максимум,
    # то перезаписываем
    if n > max_n:
        max_n = n
        count = 1
    # подсчитываем кол-во элементов,
    # равных максимальному
    elif n == max_n:
        count += 1

print(count)

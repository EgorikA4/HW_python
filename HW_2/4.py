max_len = num = 0
count_up = 0  # длина возрастающей последов.
count_down = 0  # длина убывающей последов.

while (n := int(input())) != 0:
    # первую итерацию пропускаем
    # чтобы сделать num = n,
    # поэтому и условие num != 0
    if n > num and num != 0:
        count_up += 1
    else:
        # когда возрастающая последов. прервалась
        if count_up + 1 > max_len:
            max_len = count_up + 1
        count_up = 0
    if n < num and num != 0:
        count_down += 1
    else:
        # когда убывающая последов. прервалась
        if count_down + 1 > max_len:
            max_len = count_down + 1
        count_down = 0
    num = n

# остаточные длины последов., которые не обработались в цикле
if count_down + 1 > max_len:
    max_len = count_down + 1
if count_up + 1 > max_len:
    max_len = count_up + 1

print(max_len)

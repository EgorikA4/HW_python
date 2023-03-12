n = int(input())

# запоминаем последнее число
last_num = res = 0

for i in range(n):
    num = int(input())
    if i != 0:
        # выбираем среди двух чисел минимальное -
        # это и будет возможная сумма среди двух букв
        if num < last_num:
            res += num
        else:
            res += last_num
    last_num = num

# разбили сумму строки на сумму двух соседних элементов
print(res)

count_num = 0  # кол-во чиел
summ_num = 0  # сумма чисел

# пока не ввели ноль
while (n := int(input())) != 0:
    count_num += 1  # увеличиваем счётчик
    summ_num += n  # прибавляем к сумме новове чсило
print(summ_num / count_num)

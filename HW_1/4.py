x = int(input())

# Хранится первое число в римской СС
first_num = ""

# Хранитя второе число в римской СС
second_num = ""
fl = True
if x == 100:
    print("C")
    fl = False

# получение первой цифры
elif x // 10 >= 1 and x // 10 <= 3:
    first_num = "X" * (x // 10)
elif x // 10 == 4:
    first_num = "XL"
elif x // 10 == 5:
    first_num = "L"
elif x // 10 >= 6 and x // 10 <= 8:
    first_num = "L" + "X" * (x // 10 - 5)
elif x // 10 == 9:
    first_num = "XC"
if x % 10 >= 1 and x % 10 <= 3:
    second_num = "I" * (x % 10)
elif x % 10 == 4:
    second_num = "IV"

# получение второй цифры
if x % 10 == 5:
    second_num = "V"
elif x % 10 >= 6 and x % 10 <= 8:
    second_num = "V" + "I" * (x % 10 - 5)
elif x % 10 == 9:
    second_num = "IX"
elif x % 10 == 10:
    second_num = "X"
if fl:
    print(first_num + second_num)

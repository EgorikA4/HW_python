a, b = int(input()), int(input())

# на ноль делить нельзя
if a == 0 and b != 0:
    print("NO")

# если слева будет 0x и справа 0
elif a == 0 and b == 0:
    print("INF")

elif -b % a == 0:
    print(-b // a)

# надо решить в целых числах, поэтому делаем проверку на делимость без остатка
else:
    print("NO")

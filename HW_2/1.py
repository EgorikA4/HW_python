x = int(input())

for i in range(2, x + 1):
    # идем от 2 до числа x
    # и ищем минимальный делитель
    if x % i == 0:
        print(i)
        break

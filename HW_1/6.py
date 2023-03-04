a, b, c = float(input()), float(input()), float(input())

# Вычисляем дискриминант
D = b ** 2 - 4 * a * c

# Один действ. корень
if D == 0:
    print((-1 * b) / (2 * a))

# Два действ. корня
elif D > 0:
    print(((-1 * b) + D ** 0.5) / (2 * a), ((-1 * b) - D ** 0.5) / (2 * a))

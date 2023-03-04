x1, y1 = int(input()), int(input())
x2, y2 = int(input()), int(input())

# отделяем знак(+ или -) от координат и сравниваем их
if x1 > 0:
    x1 = 0
else:
    x1 = -1

if y1 > 0:
    y1 = 0
else:
    y1 = -1

if x2 > 0:
    x2 = 0
else:
    x2 = -1

if y2 > 0:
    y2 = 0
else:
    y2 = -1

if x2 != x1 or y2 != y1:
    print("NO")
else:
    print("YES")

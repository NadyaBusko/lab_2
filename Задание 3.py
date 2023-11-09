def massiv_func(n, m):
    b = []  # двумерный массив в виде списка
    i = 0
    j = 0
    while i < n:
        j = 0
        a = []  # временный список
        while j < m:
            a.append(".")
            j += 1
            if (j == m):
                break
            a.append("*")
            j += 1
        print('  '.join(a))
        b.append(a)
        i += 1
        j = 0
        if (i == n):
            break
        a = []
        while j < m:
            a.append("*")
            j += 1
            if (j == m):
                break
            a.append(".")
            j += 1
        print('  '.join(a))
        b.append(a)
        i += 1
    print("Двумерный массив:", b)

try:
    n = int(input("Введите n = "))
    m = int(input("Введите m = "))
    massiv_func(n, m)
except ValueError:
    print("Неверно введены значения")
finally:
    print("Массив выведен.")
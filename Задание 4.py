
try:
    a = int(input("Введите делимое: "))
    b = int(input("Введите делитель: "))
    c = a/b
    if c == 1:
        raise ValueError
except ValueError:
    print("Вы ввели одинаковые числа")
except ZeroDivisionError:
    print("Невозможно деление на ноль.")
else:
    print("Результат в кубе = ", c**3)
finally:
    print(f'Мы попытались поделить {a} на {b}')
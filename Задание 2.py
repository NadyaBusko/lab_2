def function(arg):
    if isinstance(arg, dict):
        l = list(arg.keys())
        max = l[0]
        for k in arg:
            if arg[k] > arg[max]:
                max = k
        print(arg)
        print("Ключ с максимальным значением -", max, ":", arg[max])
    elif isinstance(arg, list):
        i = 0  # счетчик по списку
        index = -1  # ндекс первого отрицательного
        while i < len(arg):
            if arg[i] < 0:
                index = i
                break
            i += 1
        if index == -1:
            print(arg)
            print("Нет отрицательных элементов.")
        else:
            print(arg)
            print("Количество элементов до 1-го отрицательного =", index)
    elif isinstance(arg, int):
        i = 2
        k = 0  # покажет если число имело делители кроме 1 и самого себя
        while i <= arg // 2:
            if arg % i == 0:
                k += 1
            i += 1
        if k > 0:
            print("Число не простое")
        else:
            print("Число простое")
    elif isinstance(arg, str):
        print(arg[::-1])
        sum = 0
        k = 0
        for i in arg:
            if i.isdigit():
                ch = int(i)
                sum = sum + ch
                k += 1
        if k > 0:
            print("sum =", sum)
        else:
            print("В строке нет цифр")

dictionary = {'a': 1, 'b': 5, 'c': 2}
function(dictionary)
elements1 = [1, 5, 0, -1, 6, -7, 5]
function(elements1)
elements2 = [1, 5, 0, 1, 6, 7, 5]
function(elements2)
try:
    ch = int(input("Введите число для проверки его на простоту: "))
except ValueError:
    print("Неверно введены значения")
finally:
    print("Число введено.")
function(ch)
function("5Le2ra8")

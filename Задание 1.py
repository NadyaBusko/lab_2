def is_password_good(password):
    k = 0  # счётчик цифр
    d = 0  # счётчик заглавных букв
    for i in password:
        if i.isdigit():
            k += 1
    for i in password:
        if i.isupper():
            d += 1
    if len(password) >= 8:
        if (k > 0):
            if (d > 0):
                return True
            else:
                print("Пароль должен содержать хотя бы одну заглавную букву!")
                return False
        else:
            print("Пароль должен содержать хотя бы одну цифру!")
            return False
    else:
        print("Введите не менее 8 символов!")
        return False


a = 1
while (a):
    password = input("Введите пароль: ")
    if is_password_good(password) == True:
        print("True")
        a = 0
    else:
        print("False")

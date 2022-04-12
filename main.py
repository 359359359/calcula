print(f'Hi, who you are?')
x = 1
while x == 1:
    f_num = float(input("Введите первое число>> "))
    operand = input("Введите операцию>> ")
    s_num = float(input("Введите второе число>> "))
    if operand =='+': print(f_num + s_num)
    elif operand =='-': print(f_num - s_num)
    elif operand =='*': print(f_num * s_num)
    elif operand ==('/'): print(f_num / s_num)
    else: print('ошибка, недопустимый символ')
    print('для выхода нажать любую клавишу, для продолжения - 1')
    x = int(input())

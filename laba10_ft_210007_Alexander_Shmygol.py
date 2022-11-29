while True:
    try:
        n = int(input('Введите сумму N'))
        break
    except ValueError:
        print(" Вводите число ! ")

#1, 2, 4, 8, 16, 32 64

def summa(w):
    summa = {'k_1': 0, 'k_2': 0, 'k_4': 0, 'k_8': 0, 'k_16': 0, 'k_32': 0, 'k_64': 0, }
    s_p = w
    x = s_p // 64
    s_p = s_p - x * 64
    summa['k_64'] += x

    c = s_p // 32
    s_p = s_p - c * 32
    summa['k_32'] += c

    v = s_p // 16
    s_p = s_p - v * 16
    summa['k_16'] += v

    b = s_p // 8
    s_p = s_p - b * 8
    summa['k_8'] += b

    g = s_p // 4
    s_p = s_p - g * 4
    summa['k_4'] += g

    m = s_p // 2
    s_p = s_p - m * 2
    summa['k_2'] += m

    k = s_p // 1
    s_p = s_p - k * 1
    summa['k_1'] += k
    return print(f'{summa["k_1"]}  по 1\n'
                 f'{summa["k_2"]}  по 2\n'
                 f'{summa["k_4"]}  по 4\n'
                 f'{summa["k_8"]}  по 8\n'
                 f'{summa["k_16"]}  по 16\n'
                 f'{summa["k_32"]}  по 32\n'
                 f'{summa["k_64"]}  по 64\n')

summa(n)
























































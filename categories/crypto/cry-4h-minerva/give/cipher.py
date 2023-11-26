import random

def str_to_int(st):
    res = 0
    n = len(st)
    for i in range(n):
        res += 256**i * ord(st[n - 1 - i ]) # 256-ричная система счисления; ord() - функция, сопоставляющая символу её номер в таблице ASCII
    return res

def int_to_str(a): # кажется, здесь что-то должно было быть 🤔
    return 0

def f(x,k):
    return x**2 + a*x + k

flag = open("flag.txt","r").read()

k = random.randint(0,10**5)
a = random.randint(0,10**100)


int_flag = str_to_int(flag)

enc_flag = f(int_flag , k)
print("Функция шифрования : f (x, key) = x^2 + "+str(a)+"*x + key")
print("Зашифрованный флаг : ", enc_flag)

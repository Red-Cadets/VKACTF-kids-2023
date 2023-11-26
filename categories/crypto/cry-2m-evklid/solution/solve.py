#!/usr/bin/ python3

from Crypto.Util.number import  long_to_bytes
from pwn import *

def gcd_extended(num1, num2):
    
    if num1 == 0:
        return (num2, 0, 1)
    else:
        div, x, y = gcd_extended(num2 % num1, num1)
    return (div, y - (num2 // num1) * x, x)

s = remote('127.0.0.1', 2440)

s.recvuntil(b'N: ')
N = int(s.recvline())
print(f'N = {N}')

s.recvuntil(b'e_1: ')
e_1 = int(s.recvline())
print(f'e_1 = {e_1}')

s.recvuntil(b'e_2: ')
e_2 = int(s.recvline())
print(f'e_2 = {e_2}')

div, a, b = gcd_extended(e_1, e_2)

s.recvuntil(b': ')
s.sendline(b'3')

s.recvline()
s.recvline()
c_1 = int(s.recvline(), 16)
s.recvline()
c_2 = int(s.recvline(), 16)

flag = long_to_bytes(pow(c_1, a, N) * pow(c_2, b, N) % N)

print(flag)
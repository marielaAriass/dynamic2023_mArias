# -*- coding: utf-8 -*-
"""Recursive2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1l3Jwk7bBDSoKAc5d584vg_Nj0aMeZacX
"""

def suma(n):
    if n == 2:
        print(f'(1/{n}^2)', end='')
        return 1/n**2
    print(f'(1/{n}^2) + ', end='')
    return suma(n-1) + 1/n**2

print('='+str(suma(10)))

def suma(n):
    if n == 2:
        print(str(1/n**2), end='')
        return 1/n**2
    print(str(1/n**2)+'+', end='')
    return suma(n-1) + 1/n**2

print('='+str(suma(10)))

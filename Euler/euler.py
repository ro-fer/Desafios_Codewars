'''
# 🚀 Desafío Codewars: Múltiplos de 3 y 5

Dado un número **n**, debemos encontrar la suma de todos los múltiplos de 3 o 5 que sean menores que **n**.

Por ejemplo:
- Si el número es 10, los múltiplos de 3 o 5 debajo de 10 son **3, 5, 6, 9** y su suma es **23**.
'''

def solution(number):
    if number < 0:
        return 0
    sum= 0
    for n in range (number):
        if n % 3 == 0 or n % 5 == 0 :
            sum += n
    return sum  
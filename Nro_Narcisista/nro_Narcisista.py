'''
# 💠 Desafío Codewars: Número Narcisista

Este ejercicio trata sobre los llamados **números narcisistas** (también conocidos como **números de Armstrong**).

---

## 📝 Enunciado

Un número narcisista es un número positivo que es igual a la **suma de sus dígitos**, donde **cada dígito se eleva a la potencia del número de dígitos del número**.

Solo trabajamos con números en **base 10**.
'''

def narcissistic( value ):
    str_value = str(value)            
    cant = len(str_value)
    suma = 0
    for n in str_value:
        suma += int(n) ** cant

    return suma == value  
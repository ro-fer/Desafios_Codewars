'''
La **raíz digital** es la suma recursiva de todos los dígitos de un número hasta obtener un único dígito. 
'''

def digital_root(n):
    while n >= 10:
        suma = 0
        while n > 0:
            digito = n % 10  
            suma += digito
            n = n // 10     
        n = suma  
    print(n)

digital_root(16)
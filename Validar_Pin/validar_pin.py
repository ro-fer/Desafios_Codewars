'''
# 🔐 Desafío Codewars: Validar código PIN

> Los cajeros automáticos permiten únicamente códigos PIN formados por exactamente **4 o 6 dígitos**.  
> No se permite ningún otro carácter que no sea un número, ni longitudes diferentes.  

Tu tarea es escribir una función que tome una cadena (`string`) y devuelva:

- `True` si representa un PIN válido,
- `False` en cualquier otro caso.

'''


def validate_pin(pin):
    nro = ["1","2","3","4","5","6","7","8","9","0"]
    if len(pin) == 4 or len(pin) == 6:
        for caracter in pin:
            if caracter not in nro:
                return False
        return True
    else:
        return False
    
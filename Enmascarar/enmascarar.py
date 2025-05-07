'''
# 🛡 Desafío Codewars: Enmascarar información sensible
## 📝 Enunciado

> Normalmente, cuando compras algo en línea, te preguntan si tu número de tarjeta de crédito, número de teléfono o la respuesta a una pregunta secreta es correcta.  
> Pero como alguien podría estar mirando por encima de tu hombro, no querés que eso se muestre completamente en la pantalla.  
> En su lugar, **debe enmascararse**.

Tu tarea es escribir una función `maskify`, que **reemplace todos los caracteres de una cadena con `#`, excepto los últimos 4**.

---
'''


def maskify(cc):
    string = ""
    for index,letra in enumerate(cc):
        if index >= (len(cc)-4):
            string += letra
        else:
            string += "#"
    return string

print(maskify("HolaComoEstas"))
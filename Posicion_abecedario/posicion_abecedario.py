'''
# 🔠 Desafío Codewars: Reemplazar por Posición en el Abecedario
Dado un **string**, deberás reemplazar **cada letra** por su **posición en el alfabeto**.
'''

def alphabet_position(text):
    letras=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w", "x", "y", "z"]
    texto = ""
    text = text.lower()
    for letra in text:
        if letra.isalpha(): 
            texto += str(letras.index(letra) + 1) + " "

    return texto.strip()  


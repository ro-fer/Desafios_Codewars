'''
🧼 Desafío Codewars: ¡Eliminando las vocales de los trolls!
 Los trolls están atacando tu sección de comentarios.  
> Para detenerlos, debes eliminar todas las **vocales** de los textos que escriben.  
> Tu tarea es escribir una función que reciba una **cadena de texto** y devuelva una **nueva cadena sin vocales**.
'''
def disemvowel(string_):
    vocales = ["a","e","i","o","u","A","E","I","O","U"]
    string_sinVocales = ""
    for letra in string_ : 
        if letra in vocales:
            pass
        else:
            string_sinVocales += letra
    return string_sinVocales

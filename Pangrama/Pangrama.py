'''
# 🔤 Desafío Codewars: Detectar Pangrama
Un **pangrama** es una oración que contiene **cada letra del alfabeto** al menos una vez.  
'''

def is_pangram(st):
    letras = []
    for caracter in st.lower():
        if 'a' <= caracter <= 'z' and caracter not in letras:
            letras.append(caracter)
    
    return len(letras) == 26
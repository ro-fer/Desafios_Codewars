'''
Implementar un decodificador de codigo morse
'''

from preloaded import MORSE_CODE

def decode_morse(morse_code):
    morse_code = morse_code.strip()
    palabras_decodificadas = []
    for palabra in morse_code.split('   '):  
        letras_decodificadas = []
        for letra in palabra.split(): 
            letras_decodificadas.append(MORSE_CODE[letra])
        palabras_decodificadas.append(''.join(letras_decodificadas))
    
    return ' '.join(palabras_decodificadas)

decode_morse('.... . -.--   .--- ..- -.. .')
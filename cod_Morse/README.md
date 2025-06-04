# Decodificador de Código Morse 📡

## Descripción del Reto
Este proyecto implementa un decodificador de código Morse que convierte señales Morse en texto legible. El código Morse codifica cada carácter como una secuencia de puntos (`.`) y rayas (`-`) con las siguientes reglas:

- Caracteres individuales separados por un espacio
- Palabras separadas por tres espacios
- Espacios adicionales al inicio/final se ignoran


**Enlace al reto:** [Decode the Morse Code en Codewars](https://www.codewars.com/kata/54b724efac3d5402db00065e)

## Características
✔️ Decodificación precisa de caracteres Morse  
✔️ Manejo correcto de espacios entre palabras  
✔️ Eliminación de espacios innecesarios  
✔️ Soporte para códigos especiales como SOS  

## Cómo Usar
```python
mensaje = decode_morse('.... . -.--   .--- ..- -.. .')
print(mensaje)  # Salida: "HEY JUDE"
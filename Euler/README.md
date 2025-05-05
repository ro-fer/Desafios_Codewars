# 🚀 Desafío Codewars: Múltiplos de 3 y 5

Este desafío se basa en el **Problema 1 de Project Euler**. La tarea consiste en calcular la suma de todos los múltiplos de 3 o 5 que son menores que un número dado.

## Enunciado del problema

Dado un número **n**, debemos encontrar la suma de todos los múltiplos de 3 o 5 que sean menores que **n**.

Por ejemplo:
- Si el número es 10, los múltiplos de 3 o 5 debajo de 10 son **3, 5, 6, 9** y su suma es **23**.

**Condiciones adicionales**:
- Si el número dado es negativo, debemos devolver **0**.
- Si el número es un múltiplo tanto de 3 como de 5, solo contar uno de ellos.

## Función `solution`

La función `solution(number)` recibe un número **n** y devuelve la suma de todos los múltiplos de 3 o 5 que sean menores que **n**.

### Ejemplo de uso:

```python
print(solution(10))  # Salida esperada: 23

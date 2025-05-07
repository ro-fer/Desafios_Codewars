# 🔤 Desafío Codewars: Detectar Pangrama

Este ejercicio nos propone determinar si una frase contiene **todas las letras del abecedario al menos una vez**, sin importar mayúsculas o minúsculas. Este tipo de frases se llaman **pangramas**.

---

## 📝 Enunciado

> Un **pangrama** es una oración que contiene **cada letra del alfabeto** al menos una vez.  
> Por ejemplo, la frase `"The quick brown fox jumps over the lazy dog"` es un pangrama, ya que incluye todas las letras de la A a la Z.  
> 
> Escribí una función que reciba una cadena de texto y devuelva:
> - `True` si la cadena es un pangrama.
> - `False` si no lo es.
> 
> ✅ Ignorá números, espacios y signos de puntuación.  
> ✅ Las letras pueden estar en mayúsculas o minúsculas (no importa el caso).

---

## 🧪 Ejemplos

| Entrada                                     | Salida |
|--------------------------------------------|--------|
| `"The quick brown fox jumps over the lazy dog"` | `True` |
| `"Hello world!"`                            | `False` |
| `"Pack my box with five dozen liquor jugs"` | `True` |
| `"abcdefghijklmnoqrstuvwxyz"`               | `False` |

---

## 🧠 Lógica de la solución

1. Convertimos el texto a minúsculas para evitar diferencias entre mayúsculas y minúsculas.
2. Recorremos cada carácter del string y, si es una letra, lo agregamos a un conjunto (`set`) de letras encontradas.
3. Si el conjunto tiene 26 letras diferentes, ¡es un pangrama!



cadena = input("Ingresa una cadena de texto: ").lower()
vocales = "aeiou"
contador = 0
for palabras in cadena:
    if palabras in vocales:
        contador +=1

print(f"El numero de vocales en la cadena es: {contador}")

numeros = [7, 4, 16, 26, 9, 19, 23, 12, 3, 10]
# Primer elemento de la lista
menor = numeros[0]
for numero in numeros:
    # Modificar el valor de una variable menor si se cumple
    if numero < menor:
        menor = numero
print(menor)
    
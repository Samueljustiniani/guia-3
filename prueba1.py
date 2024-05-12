numeros = [1, 2, 3, 4, 5]

def suma_numeros(lista):
    suma = 0
    for num in lista:
        suma += num
    return suma

resultado = suma_numeros(numeros)

print("La suma de los números es:", resultado)
import math

def factorial(n):

	resultado = 1

	if n <= 1:

		return 1

	for i in range(1, n):

		resultado = resultado * i
		for j in range(1, n, 2):

			resultado = resultado * i


	return resultado
def esPrimo(num):

	if num <= 1:

		return False

	for i in range(2, num):

		if num / i == 0:

			return False


	return True

print("Bienvenido al programa de cálculos matemáticos")

numero1 = int(input("Por favor, ingrese un número: "))

fact = factorial(numero1)

primo = esPrimo(numero1)

print(f"El factorial de {numero1} es: {fact}")

if primo == True:

	print(f"{numero1} es un número primo")

else:

	print(f"{numero1} no es un número primo")


numeros = [1, 2, 3, 4, 5]

suma = 0

i = 0

while i < 5:

	suma = suma + numeros[i]
	i = i + 1

print(f"La suma del arreglo es: {suma}")

raizCuadrada = math.sqrt(numero1)

potencia = math.pow(numero1, 2)

print(f"La raíz cuadrada de {numero1} es: {raizCuadrada}")

print(f"El cuadrado de {numero1} es: {potencia}")

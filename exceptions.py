# ==== Exceptions Python ====
# ==== while True print("Hola Devs!") -> SyntaxError
# ==== 10 * 10/0 -> ZeroDivisionError
# ==== 4 + saludo*3 -> NameError
# ==== '2' + 2 -> TypeError
# ===========================

# ==== Try-except Sintaxis ====
# try:
# 	# Tu Código cuestionable va a aquí
# except:
# 	# Éste bloque se ejecuta si el código
# 	# en el bloque try tiene un excepción
# else:
# 	# Y ésto es por si quieres hacer
# 	# algo especial si el código en el bloque try
# 	# se ejecuta con éxito.

# ==== Versión 1: ====
try:
	print(8/0)
except ZeroDivisionError:
	print("No puedes dividir entre cero. BURRO!")

# ==== Versión 2 más pro ====
num1 = int( input("Ingrese el número divisor: ") )
num2 = int( input("Ingrese el número dividendo: ") )

try:
	result = num1 / num2
except ZeroDivisionError:
	print("No puedes dividir entre cero. BURRO!")
else:
	print( result )

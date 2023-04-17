"""Conversiones Básicas"""


"""
Convertir los numeros de string a enteros y luego sumarlos.
"""

numero_01 = "123"
numero_02 = "456"
numero_03 = "789"
numero_04 = "132"

# COMPLETAR - INICIO
numero_01=int(numero_01)
numero_02=int(numero_02)
numero_03=int(numero_03)
numero_04=int(numero_04)
suma_de_numeros = (numero_01+numero_02+numero_03+numero_04)
print("el resultado es:",suma_de_numeros)
# COMPLETAR - FIN

assert suma_de_numeros == 1500


"""
Convertir los numeros de enteros a string y luego concatenarlos.
"""

numero_01 = 123
numero_02 = 456
numero_03 = 789

# COMPLETAR - INICIO
numero_01 = str(numero_01)
numero_02 = str(numero_02)
numero_03 = str(numero_03)
print("los numeros son:" ,numero_01,numero_02,numero_03)
# COMPLETAR - FIN

assert suma_de_numeros_string == "123456789"


"""
Convertir los numeros de binario, octal y hexadecimal a enteros y luego
multiplicarlos.
"""

numero_binario = "0b111010110101110111101000000"
numero_octal = "0o1425"
numero_hexadecimal = "0x6f540"

# COMPLETAR - INICIO
numero_binario=int(numero_binario)
numero_octal=int(numero_octal)
numero_hexadecimal=int(numero_hexadecimal)
resultado=(numero_binario*numero_octal*numero_hexadecimal)
print(f"el resultados es:", resultado)
# COMPLETAR - FIN

assert multiplicacion_de_numeros == 44397345600000000


"""
Convertir todo los numeros a enteros y luego restarlos secuencialmente (El uno
menos el dos menos el tres menos el cuatro).
"""

numero_01 = "987"
numero_02 = "0x6f54F"
numero_03 = "0o1234"
numero_04 = 654

# COMPLETAR - INICIO
resultado_resta = int(numero_01) = int(numero_02,16)- int(numero_03,8) - numero_04
print("resultado",resultado_resta)
# COMPLETAR - FIN

assert resultado_resta == -456350

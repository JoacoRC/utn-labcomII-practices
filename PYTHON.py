a = "5"
b = "3.2"
print(a+b)
print(type(a))
"""

# ejemplo 2:
"""
a = 5
b = 3.2
print(a+b)
print(type(a))
"""

# ejemplo3:
# la \ hace que ignore el proximo caracter
# \n salto de linea, \t tabular
"""
print("hola, \"buenas tardes\"\ntodo bien?\nsi\tno")
"""

# ejemplo4:
"""
nombre = input("nombre: ")
print("tu nombre es: " + nombre)
"""
# ejemplo5:
"""
edad = input("cauntos años tenes?")
print(edad)
nueva_edad = 1+edad
print(edad)
"""

# para forzar el tipo de dato:
"""
edad = int(input("cauntos años tenes?"))
print(edad)
"""
# ejemplo6:
#mostrar datos:
"""
nombre = "sofia"
edad = 12

print("mi hija se llama {} y tiene {} años")._format_(nombre, edad)

print(f"mi hija se llama {nombre} y tiene {edad} años")



a = 2
b = 3
print(f"{a} + {b} = {a+b}")
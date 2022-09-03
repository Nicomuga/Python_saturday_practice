# Las variables son nombres que apuntan a un valor
# Y el valor es de  cierto tipo

name = "stranger"

#no pueden comenzar con  numeros ni palabras reservadas (if,def,etc)
#para seprar nombres largos se utiliza en undercore

long_name_variable="something"
longaniza="Chillán"

print(name, long_name_variable, longaniza)

#Podemos saber el tipo (Class) de la variables con la función type

print(type(longaniza),type(name),type(long_name_variable))

#otro sipor frecuentes

#int
number=42
print(type(number))

#bool
is_real= True
not_real= False
print(type(is_real),type(not_real))

#float
decimal=1.0
print(type(decimal))
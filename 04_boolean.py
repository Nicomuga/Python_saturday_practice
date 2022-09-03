#SOn formas de representar verdaderos y falsos. Un tipo de valor con solo 2 opciones: Trrue or False. Los valores se asignan siempre con T o F mayuscula al inciar

its_real= True
unreal=False

#Las comparaciones entregan o devuelven un boolean

print(10<9)
print(10>9)
print(10==9)

#ejemplo evaluando variables

limit=18
age=21

# Si (if) la edad es >= al limite de edad Se arroja el output "es mayor de edad". De lo contrario (else) se arroja el output "Es menor de edad"
if age >= limit:
    print("Es mayor de edad")
else:
    print("Es menor de edad")


#Todos los valores tienen una representacion booleana

zero=0
one=1
empty_str=""


if zero:
    print(zero, "es verdadero")
else:
    print(zero, "es falso")

if one:
    print(one, "es verdadero")
else:
    print(one, "es falso")


    #segundo ejemplo

if empty_str:
    print(empty_str, "es verdadero")
else:
    print(empty_str, "es falso")


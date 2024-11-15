from fractions import Fraction
numero1=20
numero2=40


suma = numero1 + numero2

resta = numero2 - numero1

multiplicacion = numero1 * numero2

division = numero1/ numero2

division_entera =  numero1// numero2

residuo = numero1 % numero2

potencia = numero1 ** numero2

raiz = numero1 ** (1/2)
#usando funcion para que me de resultado fraccion
fraccion = Fraction((1/3)/(1/2)).limit_denominator()


print(fraccion)
print(suma)
print(resta)
print(division)
print(division_entera)
print(residuo)
print(potencia)
print(raiz)

# de comparacion   --> (booean)

print(numero1==numero2)


# diferencia que 
print(numero1!=numero2)
# mayor que
print(numero1>numero2)

# MAyor o igual que 
print(numero1>=numero2)

# Menor  que 
print(numero1<numero2)
#menor igual que 
print(numero1<=numero2)

#logicos
print(numero1>numero2 and numero1!=numero2)
print(numero1>numero2 or numero1!=numero2)
print(not numero1<=numero2)  # lo contrario de la operacion 
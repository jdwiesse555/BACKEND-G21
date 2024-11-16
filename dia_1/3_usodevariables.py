# snake case
nombre_completo='javier wiesse'


# camelCase

nombreCompleto='javier wiesse'

#pasalCase
NombreCompleto = 'javier wiesse'

#nombre de las varibles no puedentener - @ /  y simbolos , tampoco no pueden empesar en numeros
print('.-----------------')
d3= 2-2
print(d3)

#podemos acceder al spring por su posision
print(nombreCompleto[0])
print(len(nombreCompleto))

#solo se puede visualizar el textp e sus posiciones , no se puede cambiar
# nombreCompleto[3]='p'

texto='el dia de hoy fue a clase y saque 20'

print(texto[4:10])
print(texto[:10])
print(texto[7:])


#numeros

resultado = 3 + 10.75
print(resultado)

#forma para hacer mas legible un numero grande
numerazo= 1_010_010_222
print(numerazo+1)

numero4 , numero5 = 3 , 56
print(numero5)
print(numero4)

#poner formato a un numero con redondeo
resultado = 10/9
print("{:.4f}".format(resultado))
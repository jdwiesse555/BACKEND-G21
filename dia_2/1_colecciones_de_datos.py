# listas
frutas = ['manzana','platano','papaya']
print(frutas[1])
#agrega en la lista
frutas.append('manzanas')

print(len(frutas))
#solamente si exite lo elimmara sino lanzara un error
frutas.remove('platano')
print(frutas)

#el metodo pop funciona con la Posicion de fruta y si no existe la posicion sale error 
frutas.pop(0)
print(frutas)

frutas[0]= 'kiwi'
print(frutas)
#insertar en una posicion
frutas.insert(1,'uva')
print(frutas)


# tuplas
# no son EDITABLES , una vez creada ya no puede modificar


alumnos = ('farit','francesca','cesar','cristian','eddy')
print(alumnos[0])

#crear una lista en base de tupla
copia_alumnos = list(alumnos)
#memoria que se guarda la tupla
print(id(alumnos))
print(id(copia_alumnos))

#crear tupla de una lista

segunda_copia = tuple(copia_alumnos)

#cuando copiamos una lista a otra lista lo que estamos en realidad es utulizar la misma posion de momoria
otras_frutas = frutas
print(id(frutas))
print(id(otras_frutas))
#si quiero copia a otra variable la lista hay que hacer
otras_frutas1 = frutas[:] 
otras_frutas2 = list(frutas)


frutas[1]= 'dragon'
print(frutas)
print(otras_frutas)
print(otras_frutas1)


#Set 
# es lsita desordenada y editable

inventario = {'monitores','mause','proyectores','teclados'}

print(inventario)
#no se puede hacer ()
#print(inventario[0])

inventario.add('momoria ram')
inventario.remove('mause')
print(inventario)

# sirva solo para ver si el dato existe en una seT
print('monitores' in inventario)


#dictionary 
#ordenado PERO POR LLAVES o por posicion ni indices , editable

persona = {'nombre':'eduardo','apellido':'de rivera','correo':'sada@gmail.com','edad':23,
           'hobbies':['comer','programar'],
           'direccion':{'calle':'calle los geraneos','nuemro':879,'postal':'04010'}}

print(persona)


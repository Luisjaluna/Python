#diccionarios
#los diccionarios son tipos de datos que guardan cualquier tipo de dato
# se definen:
my_dict = {"mario": 22,"luisja": 22,"rodo": 24, "ricardo": 24}
print (my_dict ["rodo"])

#objetos anidados
# 1. Lista de Listas
lista_anidada = [[10, 9, 10, 9.5], [8.5, 9, 8, 10], [10, 9, 9, 10]]

print (lista_anidada [2])

print (lista_anidada [2][3])

print (type(lista_anidada [2][3]))

# 2. Diccionario de Listas
calificaciones = {"primero": [10, 9, 10, 9.5],
		"segundo": [8.5, 9, 8, 10], 
		"tercero": [10, 9, 9, 10]}
print (calificaciones ["primero"][2])

# 3. diccionario de diccionarios
lci = {"primero": {"comercio": 8, "geopolitica": 10, "esta": 2},
	"segundo": {"micro": 7, "calculo": 8, "comercio": 10},
	"tercero": {"macro": 5, "cadena": 8, "marco": 9}}
print ("comercio internacional: ",lci ["primero"] ["comercio"])
print ("comercio exterior: ",lci ["segundo"] ["comercio"])

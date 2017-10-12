#Importamos funciones , de la libreia estandar que se llama random
import random

# 1 Lista con japones/elementos
# 2 Generar un numero aleatoreo
# 3 Imprimir la entrada de la lista con indice obtenido en el paso 2
# Hay una funcion llamada "len"
# Ej: print (len (Vec1))

hiragana = ["a", "i", "u", "e", "o", "ka", "ki", "ku", "ke", "ko","sa", "shi", "su", "se", "so", "za", "shi", "zu", "se", "so","ta", "chi", "tsu", "te", "to", "da", "ji", "tsu", "de", "do","na", "ni", "nu", "ne", "no", "ha", "hi", "hu", "he", "ho"]
indice = random.randint (0,len (hiragana)-1)
#print(indice)
print (hiragana[indice])



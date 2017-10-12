# Condicionales

# la sintaxis
"""
condicion = 18

if condicion >= 18:
	print ("Eres mayor de edad")

else:
	print ("eres menor de edad")
"""

"""
edad = int (input ("introduce tu edad: "))

if edad >= 18:
	print ("Eres mayor de edad")

else: 
	print ("eres menor de edad")
"""
"""
hambre = int (input("introduce 1 si tienes hambre o 0 si no tienes: "))
if hambre == 1:
	print ("Come no seas wey")

else:
	if hambre == 0:
		print ("Chupala")
	else: 
		print ("No mames")
"""
####################################################################################################################################################
"""
edad = int (input("introduce tu edad: "))
if edad <= 0:
	print ("Es imposible, estas loco wey")
else:
	if edad <= 18:
		print ("Eres menor de edad")
	else: 
		if edad <= 80:
			print ("Estas en tu mejor edad papi, no te fijes en lo que dice la gente")
		else:
			if edad <= 100:
				print ("Pinche cadaver")
			else: 
				if edad >= 100:
					print ("no hay, no existe")
				else:
					print ("No mames")
"""

edad = int (input("introduce tu edad: "))
if edad <= 0:
	print ("Es imposible, estas loco wey")
elif edad < 18:
	print ("Eres menor de edad")
elif edad <= 80:
	print ("Estas en tu mejor edad papi, no te fijes en lo que dice la gente")
else:
	print ("no hay, no existe")




























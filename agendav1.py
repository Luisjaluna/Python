# Contactos,
contactos = [{"nombre": "Rodolfo Ferro",
		"cel": "4771606285", 
		"e-mail": "ferro@cimat.mx"},
		{"nombre": "Mario Magaña",
		"cel": "4731111000", 
		"e-mail": "lm.magañamolina@ugto.mx"},
		{"nombre": "Luis Luna",
		"cel": "4121041850", 
		"e-mail": "lj.lunaarellano@ugto.mx"}]
# spoiler de ciclos


#for contacto in contactos:
	#print (contacto)
# contacto es una variable auxiliar y toma el valor de cada elemneto de la lista de contactos

print ("Contactos:\n")

for contacto in contactos:
	print ("Nombre:", contacto ["nombre"])
	print ("cel:", contacto ["cel"])
	print ("e-mail:", contacto ["e-mail"])
	print ()

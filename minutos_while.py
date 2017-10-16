#inicializar una variable en 0
# hay que hacer un ciclo
#

minuto,segundo = 0,0

while 1:
	print ("%d:%2d" % (minuto, segundo))
	segundo = (segundo + 1) % 60
	if segundo == 0:
		minuto = minuto + 1
	if minuto == 60 and segundo > 0: 
		break
	

import time

hora = int(time.strftime('%H'))
minutos = int(time.strftime('%M'))

if hora >= 19:
    print("Es hora de ir a casa")
else:
    print("Quedan " + str(18 - hora) + " horas y " + str(59 - minutos) + " minutos para ir a casa")

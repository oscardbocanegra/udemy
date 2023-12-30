#Práctica Módulo Datetime 1:Crea un objeto fecha llamado 
#mi_fecha que almacene el día 3 de febrero de 1999
from datetime import date, datetime

mi_fecha = date(1999, 2, 3)

#Práctica Módulo Datetime 2: Crea un objeto en la variable hoy
#que siempre almacene la fecha actual cuando sea invocada.
hoy = date.today()
print(hoy)

#Práctica Módulo Datetime 3: En una variable llamada minutos, almacena 
#únicamente los minutos de la hora actual.Por ejemplo, si se ejecutara a 
#las 20:43:17 de la noche, la variable minutos debe almacenar el valor 43
minutos = datetime.now().minute


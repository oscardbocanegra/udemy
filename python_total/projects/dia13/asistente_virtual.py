try:
    import pyttsx3
    import speech_recognition as sr
    import pywhatkit
    import yfinance as yf
    import pyjokes
    import webbrowser
    import datetime
    import wikipedia
    
except ImportError as e:
    print(f"Error de importacion: {e}")
    
# Opciones de voz / idioma    
id1 = 'spanish-latin-am'
id2 = 'spanish'
id3 = "en-uk-north"

# escuchar nuestro microfono y devolver el audio como texto
def transformar_audio_en_texto():
    
    #almacenar recognizer en variable
    r = sr.Recognizer()
    
    #configurar el microfono
    with sr.Microphone() as origen:
        
        #tiempo de espera
        r.pause_threshold = 0.8
        
        #informar que comenzo la grabacion 
        print("Ya puedes hablar")
        
        #guardar lo que escuche en el audio
        audio = r.listen(origen)
        
        try:
            # buscar en google
            pedido = r.recognize_google(audio, language="es-CO")
            
            # prueba de que pudo ingresar
            print("Dijiste: " + pedido)
            
            #devolver a pedido
            return pedido
        
        #en caso de que no entienda el audio
        except sr.UnknownValueError:
            
            #prueba de que no crompendio el audio
            print("ups, no entendi")
            
            #devolver error
            return "Sigo esperando"
        
        #en caso de no resolver el pedido 
        except sr.RequestError:
            
            #prueba de que no crompendio el audio
            print("ups no hay servicio")
            
            #devolver error
            return "Sigo esperando"
        
        #error inesperado
        except:
            
            #prueba de que no crompendio el audio
            print("ups, algo salio mal")
            
            #devolver error
            return "Sigo esperando"
        
#funcion para que el asistente pueda ser escuchado
def hablar(mensaje):
    
    # encender el motor de pytts3
    engine = pyttsx3.init()
    engine.setProperty('voice', id1)
    
    # pronunciar mensaje
    engine.say(mensaje)
    engine.runAndWait()

#Informar el dia de la semana
def pedir_dia():
    
    #crear variable con datos actuales
    dia = datetime.date.today()
    print(dia)
    
    # Crear variable para el dia de la semana 
    dia_semana = dia.weekday()
    print(dia_semana)
    
    # diccionario con nombre de dias
    calendario = {0: 'Lunes',
                  1: 'Martes',
                  2: 'Miércoles',
                  3: 'Jueves',
                  4: 'Viernes',
                  5: 'Sábado',
                  6: 'Domingo'}
    
    # decir dia de la semana
    hablar(f"Today's {calendario[dia_semana]}")

def pedir_hora():
    
    #pedir una variable con datos de la hora
    hora = datetime.datetime.now()
    print(hora)
    hora = f"En este momento son las {hora.hour} horas con {hora.minute} y {hora.second} segundos"
    
    hablar(hora)
    
pedir_hora()
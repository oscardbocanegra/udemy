from tkinter import *

#iniciar tkinter
aplicacion = Tk()

#Tamaño de la ventana
aplicacion.geometry('1020x630+0+0')

#Evitar maximizar
aplicacion.resizable(0, 0)

#titulo de la ventana
aplicacion.title("Mi restaurante - Sistema de facturacion")

#color de fondo de la ventana
aplicacion.config(bg="burlywood")

#color de fondo de la ventana 
aplicacion.config(bg='burlywood')

#panel superiror
panel_superior = Frame(aplicacion, bd=1, relief=FLAT)
panel_superior.pack(side=TOP)

#etiqueta titulo
etiqueta_titulo = Label(panel_superior, text='Sistema de facturacion', fg='azure4',
                        font=('Dosis', 58), bg='burlywood', width=27)

etiqueta_titulo.grid(row=0, column=0)

#panel izquierdo
panel_izquierdo = Frame(aplicacion, bd=1, relief=FLAT)
panel_izquierdo.pack(side=LEFT)

#panel costos
panel_costos = Frame(panel_izquierdo, bd=1, relief= FLAT)
panel_costos.pack(side=BOTTOM)

#panel comidas
panel_comidas = LabelFrame(panel_izquierdo, text='Comida', font=('Dosis', 19, 'bold'),
                           bd=1, relief=FLAT, fg='azure4')
panel_comidas.pack(side=LEFT)

#panel bebidas
panel_bebidas = LabelFrame(panel_izquierdo, text='Bebida', font=('Dosis', 19, 'bold'),
                           bd=1, relief=FLAT, fg='azure4')
panel_bebidas.pack(side=LEFT)


#panel postres
panel_postres = LabelFrame(panel_izquierdo, text='Postre', font=('Dosis', 19, 'bold'),
                           bd=1, relief=FLAT, fg='azure4')
panel_postres.pack(side=LEFT)

#panel derecha
panel_derecha = Frame(aplicacion, bd=1, relief=FLAT)
panel_derecha.pack(side=RIGHT)

#panel calculadora
panel_calculadora = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
panel_calculadora.pack()

#panel recibo
panel_recibo = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
panel_recibo.pack()

#panel botones
panel_botones = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
panel_botones.pack()

#lista de productos
lista_comidas = ['pollo', 'carne', 'pescado', 'pizza', 'hamburguesa', 'salchipapa', 'arroz', 'picada']
lista_bebidas = ['agua', 'soda', 'jugo', 'cocacola', 'vino1', 'vino2', 'cerveza1', 'cerveza2']
lista_postres = ['helado', 'fruta', 'brownies', 'flan', 'mousse', 'pastel1', 'pastel2', 'pastel3']

#generar items comida 
variables_comida = []
contador = 0
for comida in lista_comidas:
    variables_comida.append('')
    variables_comida[contador] = IntVar()
    comida = Checkbutton(panel_comidas, text=comida.title(), font=('Dosis', 19, 'bold'),
                         onvalue=1, offvalue=0, variable=variables_comida[contador])
    
    comida.grid(row=contador, column=0, sticky=W)
    contador += 1
    
#generar items bebida 
variables_bebida = []
contador = 0
for bebida in lista_bebidas:
    variables_bebida.append('')
    variables_bebida[contador] = IntVar()
    bebida = Checkbutton(panel_bebidas, text=bebida.title(), font=('Dosis', 19, 'bold'),
                         onvalue=1, offvalue=0, variable=variables_bebida[contador])
    
    bebida.grid(row=contador, column=0, sticky=W)
    contador += 1
    
#generar items postres 
variables_postres = []
contador = 0
for postres in lista_postres:
    variables_postres.append('')
    variables_postres[contador] = IntVar()
    postres = Checkbutton(panel_postres, text=postres.title(), font=('Dosis', 19, 'bold'),
                         onvalue=1, offvalue=0, variable=variables_postres[contador])
    
    postres.grid(row=contador, column=0, sticky=W)
    contador += 1

#Evitar que la aplicacion se cierre
aplicacion.mainloop()
from tkinter import *
import parser

# creo una ventana para mi aplicación 
root = Tk()
root.title("Calculator")

# Defino el cuadro de entrada de la cuenta a realizar
display= Entry(root)
display.grid(row=1,columnspan=6, sticky=W+E)

#indice de que posición estoy en la pantalla, se incrementa
# cada vez que toco una tecla
i= 0

# función para mostrar en el cuadro de cálculo el número de la
# tecla seleccionada
def get_numbers(n):
    global i
    display.insert(i, n)
    i+=1

# función para obtener el botón de operación seleccionado
def get_operation(operator):
    global i
    operator_lenght= len(operator)
    display.insert(i, operator)
    i +=operator_lenght

# función para limpiar la pantalla
def clear_display():
    display.delete(0,END)

# función para borrar el último número ingresado 
def undo():
    display_state = display.get()
    if len(display_state):
        display_new_state=display_state[:-1]
        clear_display()
        display.insert(0,display_new_state)
    else:
        clear_display()
        display.insert(0,"error")

# función para realizar el cálculo solicitado
def calculate():
    display_state= display.get()
    try:
        math_expression =parser.expr(display_state).compile()
        result = eval(math_expression)
        clear_display()
        display.insert(0,result)
    except math_expression as identifier:
        clear_display()
        display.insert(0,"error")

# ubico los botones clickeables en pantalla
#numeric buttons
Button(root,text="1", command=lambda:get_numbers(1)).grid(row=2,column=0, sticky=W+E)
Button(root,text="2", command=lambda:get_numbers(2)).grid(row=2,column=1, sticky=W+E)
Button(root,text="3", command=lambda:get_numbers(3)).grid(row=2,column=2, sticky=W+E)

Button(root,text="4", command=lambda:get_numbers(4)).grid(row=3,column=0, sticky=W+E)
Button(root,text="5", command=lambda:get_numbers(5)).grid(row=3,column=1, sticky=W+E)
Button(root,text="6", command=lambda:get_numbers(6)).grid(row=3,column=2, sticky=W+E)

Button(root,text="7", command=lambda:get_numbers(7)).grid(row=4,column=0, sticky=W+E)
Button(root,text="8", command=lambda:get_numbers(8)).grid(row=4,column=1, sticky=W+E)
Button(root,text="9", command=lambda:get_numbers(9)).grid(row=4,column=2, sticky=W+E)

Button(root,text="0", command=lambda:get_numbers(0)).grid(row=5,column=1, sticky=W+E)

# Botones parte 2 (simbolos y operaciones)
Button(root,text="AC", command=lambda:clear_display()).grid(row=5,column=0, sticky=W+E)
Button(root,text="%", command=lambda:get_numbers("%")).grid(row=5,column=2, sticky=W+E)

Button(root,text="+", command=lambda:get_numbers("+")).grid(row=2,column=3,sticky=W+E)
Button(root,text="-", command=lambda:get_numbers("-")).grid(row=3,column=3,sticky=W+E)
Button(root,text="*", command=lambda:get_numbers("*")).grid(row=4,column=3,sticky=W+E)
Button(root,text="/", command=lambda:get_numbers("/")).grid(row=5,column=3,sticky=W+E)

Button(root,text="←", command=lambda:undo()).grid(row=2,column=4,sticky=W+E, columnspan=2)
Button(root,text="exp", command=lambda:get_numbers("**")).grid(row=3,column=4,sticky=W+E)
Button(root,text="^2", command=lambda:get_numbers("**2")).grid(row=3,column=5,sticky=W+E)
Button(root,text="(", command=lambda:get_numbers("(")).grid(row=4,column=4,sticky=W+E)
Button(root,text=")", command=lambda:get_numbers(")")).grid(row=4,column=5,sticky=W+E)
Button(root,text="=", command=lambda:calculate()).grid(row=5,column=4,sticky=W+E,columnspan=2)

#comienza el loop del programa principal
root.mainloop()
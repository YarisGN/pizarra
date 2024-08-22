# Libreria para crear las ventanas, importar 
from tkinter import *

#Instancia para tener la ventana
window = Tk()
window.title("Pizarra")

# Agregar un wichep que sera un Canvas en el que podremos dibujar
canvas = Canvas(window, width=800, height=600, bg='black')
canvas.pack()

is_drawing = False # Variable para detectar cuando estamos dibujando
last_x, last_y = 0,0 # Dos variables para saber donde estaban la dos ultimas coordenadas de nuestro raton
lines = [] # Guardar las lineas que se han dibujado


# Funcion cuando haga click con el raton
def start_drawing(event): # Llamara la funcion y le pasara el evento
    global is_drawing, last_x, last_y # Indica que ahora estamos dibujando y actualiza las coordenadas del raton
    is_drawing = True # Ahora es cierto que estamos dibujando
    last_x, last_y = event.x, event.y # Las ultimas coordenadas son las que pse el evento

canvas.bind('<Button-1>', start_drawing) 


# Funcion que recibe el evento
def stop_drawing(event):
    global is_drawing #modificar el estado de is_drawing
    is_drawing = False

canvas.bind('<ButtonRelease-1>', stop_drawing)

# Funcion que va a leer y en caso que este dibujando, creara una linea
def draw(event):
    global last_x, last_y
    if is_drawing:
        line = canvas.create_line(last_x, last_y, event.x, event.y, fill='white')
        lines.append(line) # Guardar en la lista de lineas
        last_x, last_y = event.x, event.y # Que las ultimas coordenadas sean las que devuelve el evento
canvas.bind('<B1-Motion>', draw)


# Shorcat, para eliminar la ultima linea
def undo(event):
    if lines:
        canvas.delete(lines.pop())
window.bind('<Control-z>', undo)

#empaquetar wichep para que sea parte de mi ventana 
window.mainloop()

# GUI elements that move
# from BroCode

from tkinter import *


def scale_submit():
    print("The temperature is: " + str(scale.get()) + " degreesC")


# drag and drop functions
def drag_start(event):
    widget = event.widget
    widget.startX = event.x
    widget.startY = event.y

def drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget.startX + event.x
    y = widget.winfo_y() - widget.startY + event.y
    widget.place(x=x, y=y)

def move_up(event):
    logo_label.place(x=logo_label.winfo_x(), y=logo_label.winfo_y()-10)

def move_down(event):
    logo_label.place(x=logo_label.winfo_x(), y=logo_label.winfo_y()+10)

def move_left(event):
    logo_label.place(x=logo_label.winfo_x()-10, y=logo_label.winfo_y())


def move_right(event):
    logo_label.place(x=logo_label.winfo_x()+10, y=logo_label.winfo_y())


# keyboard and mouse events
def doSomething(event):
    print(f"Mouse coordinates: {event.x}, {event.y}")
    # key_label.config(text=event.keysym)


# main window generation starts here *****************************
window = Tk()
window.title("Here is my Project")
window.config(background="cyan")

# from BroCode
icon = PhotoImage(file='m3-blue-icon.png')
window.iconphoto(True, icon)

window.bind("<w>", move_up)
window.bind("<s>", move_down)
window.bind("<a>", move_left)
window.bind("<d>", move_right)
window.bind("<Up>", move_up)
window.bind("<Down>", move_down)
window.bind("<Left>", move_left)
window.bind("<Right>", move_right)

# My Photo from original test project
my_logo = PhotoImage(file="ConsultLogo2.png")
logo_label = Label(window, image=my_logo, bg='cyan')
# logo_label.grid(row=0, column=1, columnspan=2)
logo_label.place(x=100, y=100)

# drag and drop bindings
# logo_label.bind("<Button-1>", drag_start)
# logo_label.bind("<B1-Motion>", drag_motion)

# scale = sliding numeric control
scale_frame = Frame(window, bg='white', bd=3, relief=RIDGE)
scale_frame.grid(row=9, column=1, columnspan=4, padx=20, pady=10)
# drag and drop bindings
scale_frame.bind("<Button-1>", drag_start)
scale_frame.bind("<B1-Motion>", drag_motion)

scale_cold = PhotoImage(file='icons8-snowflake-48.png')
cold_label = Label(scale_frame, image=scale_cold, bg='cyan')
cold_label.grid(row=9, column=0, padx=20, sticky=E)

scale = Scale(scale_frame,
              from_=0,
              to=100,
              length=400,
              orient=HORIZONTAL,
              font=('FreeMono', 11, 'bold'),
              tickinterval=10,          # displays numbers along scale
              #showvalue=0,            # hide current value
              #resolution=5,              # create steps
              troughcolor='#00FF00',
              fg='#FF4800',
              bg='#111111',)
scale.set(((scale['from']-scale['to'])/2) + scale['to'])               # starting value in middle
scale.grid(row=9, column=1, pady=20)

scale_hot = PhotoImage(file='icons8-fire-48.png')
hot_label = Label(scale_frame, image=scale_hot, bg='cyan')
hot_label.grid(row=9, column=2, padx=20, sticky=W)

scale_button = Button(scale_frame, text='read scale', command=scale_submit)
scale_button.grid(row=9, column=3, padx=20)


# canvas = widget that is used to draw graphs, plots, images in a window
canvas = Canvas(window, height=250, width=400)
# greenLine = canvas.create_line(0, 0, 400, 250, fill="green", width=5)
# redLine = canvas.create_line(0, 250, 400, 0, fill="red", width=5)
# canvas.create_rectangle(50, 50, 350, 200, fill="purple")
# canvas.create_polygon(200, 0, 350, 250, 50, 250, fill="yellow")
# points = [200, 0, 350, 100, 300, 250, 100, 250, 50, 100]
points = [250, 10, 390, 100, 330, 240, 170, 240, 90, 100]
canvas.create_polygon(points, fill="yellow", outline="black", width=3)
# canvas.create_arc(0, 0, 250, 250, fill="blue", style=PIESLICE, start=90, extent=180)
canvas.create_arc(10, 10, 240, 240, fill="red", extent=180, width=10)
canvas.create_arc(10, 10, 240, 240, fill="white", extent=180, start=180, width=10)
canvas.create_oval(80, 90, 170, 160, fill="white", width=10)
canvas.grid(row=16, column=2, columnspan=3, padx=5)

# keyboard key events
# window.bind("<Key>", doSomething)   # keyboard key (sends key name)
# key_label = Label(window, font=("FreeSerif", 100))
# key_label.grid(row=17, column=1)
# mouse key events
window.bind("<Button-1>", doSomething)  # left mouse click
# window.bind("<Button-2>", doSomething)  # Scroll wheel or center mouse click
# window.bind("<Button-3>", doSomething)  # right mouse click
# window.bind("<ButtonRelease>", doSomething)  # any mouse button release
# window.bind("<Enter>", doSomething)     # mouse enter window or object
# window.bind("<Leave>", doSomething)     # mouse leave the window
# window.bind("<Motion>", doSomething)    # where the mouse moved


# run main loop
window.mainloop()

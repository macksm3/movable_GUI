# GUI elements that move
# from BroCode

import tkinter as tk
from Ball import Ball
from Pics import Pics
import time

WIDTH = 900
HEIGHT = 400
xVelocity = 3
yVelocity = 2


# run = False

def main():
    def run_animation():
        while run.get():  # get value of variable run from checkbutton
            volley_ball.move()
            tennis_ball.move()
            basket_ball.move()
            # football.move()
            mack_icon.move()
            parrot_icon.move()
            usb_icon.move()
            sdCard_icon.move()
            gecko_icon.move()
            window.update()
            time.sleep(0.01)
            check_button_text.set("Animation Running")
        else:
            check_button_text.set("Run Animation")

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
        canvas.move(canvas_image, 0, -10)
        logo_label.place(x=logo_label.winfo_x(), y=logo_label.winfo_y() - 10)

    def move_down(event):
        canvas.move(canvas_image, 0, 10)
        logo_label.place(x=logo_label.winfo_x(), y=logo_label.winfo_y() + 10)

    def move_left(event):
        canvas.move(canvas_image, -10, 0)
        logo_label.place(x=logo_label.winfo_x() - 10, y=logo_label.winfo_y())

    def move_right(event):
        canvas.move(canvas_image, 10, 0)
        logo_label.place(x=logo_label.winfo_x() + 10, y=logo_label.winfo_y())

    # keyboard and mouse events
    def doSomething(event):
        print(f"Mouse coordinates: {event.x}, {event.y}")
        # key_label.config(text=event.keysym)

    # main window generation starts here *****************************
    window = tk.Tk()
    window.geometry("1000x1000")
    window.title("Movable objects in GUI")
    window.config(background="cyan")

    # from BroCode
    icon = tk.PhotoImage(file='m3-blue-icon.png')
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
    my_logo = tk.PhotoImage(file="ConsultLogo2.png")
    logo_label = tk.Label(window, image=my_logo, bg='cyan')
    # logo_label.grid(row=0, column=1, columnspan=2)
    logo_label.place(x=250, y=100)

    # drag and drop bindings
    # logo_label.bind("<Button-1>", drag_start)
    # logo_label.bind("<B1-Motion>", drag_motion)

    # scale = sliding numeric control
    scale_frame = tk.Frame(window, bg='white', bd=3, relief="ridge")
    # scale_frame.grid(row=9, column=1, columnspan=4, padx=20, pady=10)
    scale_frame.place(x=150, y=850)
    # drag and drop bindings
    scale_frame.bind("<Button-1>", drag_start)
    scale_frame.bind("<B1-Motion>", drag_motion)

    scale_label = tk.Label(scale_frame, text="drag with mouse to move", font=("Comic Sans MS", 12), bg="white")
    scale_label.grid(row=0, column=0, columnspan=4)

    scale_cold = tk.PhotoImage(file='icons8-snowflake-48.png')
    cold_label = tk.Label(scale_frame, image=scale_cold, bg='cyan')
    cold_label.grid(row=9, column=0, padx=20, sticky="E")

    scale = tk.Scale(scale_frame,
                     from_=0,
                     to=100,
                     length=400,
                     orient="horizontal",
                     font=('FreeMono', 11, 'bold'),
                     tickinterval=10,  # displays numbers along scale
                     # showvalue=0,            # hide current value
                     # resolution=5,              # create steps
                     troughcolor='#00FF00',
                     fg='#FF4800',
                     bg='#111111', )
    scale.set(((scale['from'] - scale['to']) / 2) + scale['to'])  # starting value in middle
    scale.grid(row=9, column=1, pady=20)

    scale_hot = tk.PhotoImage(file='icons8-fire-48.png')
    hot_label = tk.Label(scale_frame, image=scale_hot, bg='cyan')
    hot_label.grid(row=9, column=2, padx=20, sticky="W")

    scale_button = tk.Button(scale_frame, text='read scale', command=scale_submit)
    scale_button.grid(row=9, column=3, padx=20)

    checkbox_photo = tk.PhotoImage(file='unchecked_icon.png')
    checked_photo = tk.PhotoImage(file='checked_icon.png')
    run = tk.BooleanVar()
    check_button_text = tk.StringVar()
    check_button_text.set("Run Animation")
    check_button = tk.Checkbutton(window,
                                  text="Run Animation",
                                  onvalue=True,
                                  offvalue=False,
                                  variable=run,
                                  textvariable=check_button_text,
                                  command=run_animation,
                                  font=('Ink Free', 20),
                                  fg="blue",
                                  bg="yellow",
                                  activeforeground='black',
                                  activebackground='grey',
                                  padx=25,
                                  pady=10,
                                  image=checkbox_photo,
                                  selectimage=checked_photo,
                                  compound='left',
                                  selectcolor='#00FF88',
                                  indicatoron=False,
                                  relief='raised',
                                  bd=4,
                                  )
    # check_button.grid(row=4, column=1)
    check_button.place(x=650, y=0)

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

    # exit button from original test project
    quit_button = tk.Button(window, text="Exit Program", width=15, command=window.quit)
    # quit_button.grid(row=31, column=0, columnspan=5, sticky=S)
    quit_button.place(x=0, y=0)

    move_it_label = tk.Label(window, text="Use arrow keys to move stuff", font=("Ink Free", 20, "bold"), bg="cyan")
    move_it_label.place(x=200, y=0)

    # canvas = widget that is used to draw graphs, plots, images in a window
    canvas = tk.Canvas(window, height=HEIGHT, width=WIDTH)
    # greenLine = canvas.create_line(0, 0, 400, 250, fill="green", width=5)
    # redLine = canvas.create_line(0, 250, 400, 0, fill="red", width=5)
    # canvas.create_rectangle(50, 50, 350, 200, fill="purple")
    # canvas.create_polygon(200, 0, 350, 250, 50, 250, fill="yellow")
    # points = [200, 0, 350, 100, 300, 250, 100, 250, 50, 100]
    # points = [250, 10, 390, 100, 330, 240, 170, 240, 90, 100]
    # canvas.create_polygon(points, fill="yellow", outline="black", width=3)
    # canvas.create_arc(0, 0, 250, 250, fill="blue", style=PIESLICE, start=90, extent=180)
    # canvas.create_arc(10, 10, 240, 240, fill="red", extent=180, width=10)
    # canvas.create_arc(10, 10, 240, 240, fill="white", extent=180, start=180, width=10)
    # canvas.create_oval(80, 90, 170, 160, fill="white", width=10)
    # canvas.grid(row=16, column=2, columnspan=3, padx=5)
    canvas.place(x=50, y=350)

    # background_photo = PhotoImage(file='brushed_400x400_light.png')
    # background = canvas.create_image(0, 0, image=background_photo, anchor=NW)

    cp_image = tk.PhotoImage(file='icons8-control-panel-64.png')
    canvas_image = canvas.create_image(450, 200, image=cp_image)

    gecko_image = tk.PhotoImage(file='icons8-lizard-48.png')
    sdCard_image = tk.PhotoImage(file='icons8-sd-48.png')
    usb_image = tk.PhotoImage(file='icon_usbstick_78x89.png')
    parrot_image = tk.PhotoImage(file='icons8-parrot-96.png')
    mack_image = tk.PhotoImage(file='icons8-mack-48.png')
    # ani_image = tk.canvas.create_image(0, 0, image=mack_image, anchor=NW)

    # image_width = mack_image.width()
    # image_height = mack_image.height()

    # while True:
    #     coordinates = canvas.coords(ani_image)
    #     # print(coordinates)
    #     if coordinates[0] >= (WIDTH - image_width) or coordinates[0] < 0:
    #         xVelocity = -xVelocity
    #     if coordinates[1] >= (HEIGHT - image_height) or coordinates[1] < 0:
    #         yVelocity = -yVelocity
    #     canvas.move(ani_image, xVelocity, yVelocity)
    #     window.update()
    #     time.sleep(0.01)

    volley_ball = Ball(canvas, 0, 0, 100, 2, 3, "white")
    tennis_ball = Ball(canvas, 0, 0, 50, 4, 5, "yellow")
    basket_ball = Ball(canvas, 0, 0, 120, 8, 7, "orange")
    # football = Ball(canvas, 0, 0, 80, 5, 6, "brown")

    mack_icon = Pics(canvas, 50, 50, 3, 5, mack_image)
    parrot_icon = Pics(canvas, 100, 100, 9, 12, parrot_image)
    sdCard_icon = Pics(canvas, 60, 60, 7, 5, sdCard_image)
    usb_icon = Pics(canvas, 80, 80, 3, 2, usb_image)
    gecko_icon = Pics(canvas, 25, 25, 5, 7, gecko_image)

    # run main loop
    window.mainloop()


if __name__ == '__main__':
    main()

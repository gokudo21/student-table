from guizero import App, Text, TextBox, PushButton, Slider, Picture , Window ,CheckBox ,info
import subprocess

x = 0
y = 0
z = 0
def do_booking():
    info("order", "your order was sent to the magsaf")
def close():
    app.destroy()

def juiceno():
    global x
    x = x + 1
    order.value = x
def snackno():
    global y
    y = y + 1
    order2.value = y
def sandno():
    global z
    z = z + 1
    order3.value = z

app = App(layout="grid")
app.tk.attributes("-fullscreen",True)
sandwich = PushButton(app, text="sandwich",command=sandno ,image="krwa.gif", grid=[1,4], align="left",width=250, height=150)
juice = PushButton(app, text="juice",command=juiceno ,image="kdd.gif", grid=[1,5], align="left",width=130, height=200)
snack = PushButton(app, text="snack",command=snackno, image="spal.gif", grid=[1,6], align="left",width=130, height=200)

order3 = Text(app, text=x , grid=[4,4] )
order = Text(app, text=y , grid=[4,5] )
order2 = Text(app, text=z , grid=[4,6] )




book_seats = PushButton(app, command=do_booking, text="send order",width=30, height=5 , grid=[4,15], align="left")
button = PushButton(app,text="خروج", command=close ,width=30, height=5 , grid=[7,15],align="bottom")
app.display()

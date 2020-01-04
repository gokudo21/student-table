from guizero import App, Text, TextBox, PushButton, Slider, Picture , Window
import subprocess

def close():
    app.destroy()

app = App(title="cccccccc")
Picture(app, image="2.gif")

app.tk.attributes("-fullscreen",True)

button = PushButton(app,text="close", command=close)


app.display()

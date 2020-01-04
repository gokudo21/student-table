from guizero import App, Text, TextBox, PushButton, Slider, Picture , Window
import subprocess


app = App(layout="grid")


def button1():
    subprocess.run("python 1.py", shell=True)
def button2():
    subprocess.run("python magsaf.py", shell=True)

def close():
    app.destroy()


#app = App(title="aaaaaaaaaaaaaaaaa")

welcome_message = Text(app, text="Welcome YOUSEF", size=40, font="Times new roman", color="lightblue" , grid=[1,0])


app.tk.attributes("-fullscreen",True)
PushButton(app, text="جدول الحصص", grid=[0,0])
button = PushButton(app,text="مواعيد الحصص", command=button1 , grid=[2,0],align="left")
button = PushButton(app,text="التقويم الدراسي", command=button2 , grid=[3,0] ,align="left")
button = PushButton(app,text="magsaf", command=button2 , grid=[3,1] ,align="left")
button = PushButton(app,text="light", command=button2 , grid=[3,2] ,align="left")
button = PushButton(app,text="خروج", command=close ,width=30, height=5 , grid=[4,0],align="bottom")


app.display()


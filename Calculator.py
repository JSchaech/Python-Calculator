import guizero
from guizero import App,Text,PushButton,Box

def button_clicked():
    sInput = "3"
    message.value= sInput

def addNum(x):
    global sInput
    sInput = sInput + str(x)
    message.value = sInput

def add_operator(operator):
    global sInput
    sInput = sInput + operator
    message.value = sInput

def clear_input():
    global sInput
    sInput = ""
    message.value = sInput

def get_value():
    global sInput
    if not(sInput[0].isdigit()):
        print("Error Wrong Syntax")
        message.value = "ERROR FALSE SYNTAX"
    else:
        print(eval(sInput))
        sInput = str(eval(sInput))
        message.value = sInput



app = App("Calculator")
message = Text(app, text="")
button_box = Box(app, layout="grid")
sInput = ""

for i in range(3):
    for j in range(3):
        num = i * 3 + j + 1
        button = PushButton(button_box, text=str(num), command=addNum, args=[num], grid=[j, i])

zero_button = PushButton(button_box, text="0", command=addNum, args=[0], grid=[1, 3])

# Operator buttons
add_button = PushButton(button_box, text="+", command=add_operator, args=["+"], grid=[3, 0])
subtract_button = PushButton(button_box, text="-", command=add_operator, args=["-"], grid=[3, 1])
multiply_button = PushButton(button_box, text="*", command=add_operator, args=["*"], grid=[3, 2])
divide_button = PushButton(button_box, text="/", command=add_operator, args=["/"], grid=[3, 3])

# Clear button
clear_button = PushButton(button_box, text="C", command=clear_input, grid=[0, 3])

# Clac Button
clac_Button = PushButton(button_box, text="=",command=get_value,grid=[2,3])


app.display()

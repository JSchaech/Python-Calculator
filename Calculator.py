from guizero import App,Text,PushButton,Box

#-----------------------------------------------------------------------------------#
#   Define Needed Functions

def addNum(x): # Add Numbers when Button Pressed
    global sInput
    sInput = sInput + str(x)
    message.value = sInput

def add_operator(operator): # Add Operator(+,/,-,*) when pressed
    global sInput
    sInput = sInput + operator
    message.value = sInput

def clear_input(): # Clear Everythinh
    global sInput
    sInput = ""
    message.value = sInput

def del_input():
    global sInput
    sInput = sInput[:-1]
    message.value = sInput

def get_value():
    global sInput
    if not(sInput[0].isdigit()) and not(sInput[0]== "-"):
        message.value = "ERROR FALSE SYNTAX" # Display Error Message
    else:
        print(eval(sInput)) # used for Debuging
        sInput = str(eval(sInput))
        message.value = sInput

#-----------------------------------------------------------------------------------#

sInput = ""

app = App("Calculator") # Create GuiZero App

border_box = Box(app, width="fill", height="fill", layout="grid")
border_box.bg = "black"
button_box = Box(app, layout="grid") # Create Grid For Buttons

message = Text(border_box, text="",color="white",grid=[0,0]) # Create Text Field for Clacualtion

button_height = 2
button_Width = button_height * 4

#-----------------------------------------------------------------------------------#

for i in range(3):
    for j in range(3):
        num = i * 3 + j + 1
        button = PushButton(button_box, text=str(num), command=addNum, args=[num], grid=[j, i],width=button_Width,height=button_height)

zero_button = PushButton(button_box, text="0", command=addNum, args=[0], grid=[1, 3],width=button_Width,height=button_height)

# Operator buttons
add_button = PushButton(button_box, text="+", command=add_operator, args=["+"], grid=[3, 0],width=button_Width,height=button_height)
subtract_button = PushButton(button_box, text="-", command=add_operator, args=["-"], grid=[3, 1],width=button_Width,height=button_height)
multiply_button = PushButton(button_box, text="*", command=add_operator, args=["*"], grid=[3, 2],width=button_Width,height=button_height)
divide_button = PushButton(button_box, text="/", command=add_operator, args=["/"], grid=[3, 3],width=button_Width,height=button_height)

# Clear button
clear_button = PushButton(button_box, text="C", command=clear_input, grid=[4, 0],width=button_Width,height=button_height)

#dot button
dot_button = PushButton(button_box, text=".", command=add_operator, args=["."], grid=[2, 3],width=button_Width,height=button_height)

#Del button
del_button = PushButton(button_box, text="<<", command=del_input,grid=[4, 1],width=button_Width,height=button_height)

# Clac Button
clac_Button = PushButton(button_box, text="=",command=get_value,grid=[0,3],width=button_Width,height=button_height)

#-----------------------------------------------------------------------------------#

app.display()

import PySimpleGUI as sg
from caculate import caculator
import re

def change_operator(eq):
    eq = eq.replace('sin', '!')
    eq = eq.replace('cos', '@')
    eq = eq.replace('tan', '#')
    eq = eq.replace('pi', '180')
    return eq

def calculate(inputs):
    str_eq = ""
    cache = ""
    ca_status = False
    mybutton = lambda x: sg.B(x, size=(5, 1))
    layout = [
        [sg.Input(inputs, key="INPUT")],
        [mybutton(f"{i}") for i in range(7, 10)] + [mybutton("+")],
        [mybutton(f"{i}") for i in range(4, 7)]
        + [mybutton("-"), mybutton("sin"), mybutton("pi")],
        [mybutton(f"{i}") for i in range(1, 4)]
        + [mybutton("*"), mybutton("cos"), mybutton("C")],
        [
            mybutton("."),
            mybutton("0"),
            mybutton("="),
            mybutton("/"),
            mybutton("tan"),
            mybutton("L"),
        ],
    ]
    window = sg.Window("响存计算器", layout)
    while 1:
        event, values = window.read()
        if event in (None, "Exit"):
            break
        if event == "=":
            ca_status = True
            str_eq = change_operator(window["INPUT"].get())
            answer = caculator.caculator(str_eq)
            cache = str(answer)
            window["INPUT"].update(str(answer))
            print(change_operator(str_eq))
        elif event == "C":
            str_eq = ""
            window["INPUT"].update("")
        elif event == "L":
            window["INPUT"].update(window["INPUT"].get() + cache)
        else:
            if event == "sin":
                print(window["INPUT"].get())
            if event == "cos":
                print(window["INPUT"].get())
            if event == "tan":
                print(window["INPUT"].get())
            else:
                if ca_status:
                    ca_status = False
                    window["INPUT"].update("")
                window["INPUT"].update(window["INPUT"].get() + event)
    window.close()


if __name__ == "__main__":
    calculate(None)

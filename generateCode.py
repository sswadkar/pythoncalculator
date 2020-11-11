import pynput
from pynput.keyboard import Key, Controller
import time
keyboard = Controller()
sign = ["+","-","*","/"]
time.sleep(2)
for x in range(0,100):
    for y in range(100):
        for z in range(len(sign)):
            if sign[z] == "/":
                if y != 0:
                    ans = eval(str(x) + " " + sign[z] + " " + str(y))
                    time.sleep(0.6)
                    keyboard.type("if userinput1 == " + str(x) + " and sign == " + '"' + str(sign[z]) + '"' + " and userinput2 == " + str(y) +":")
                    keyboard.press(Key.enter)
                    keyboard.release(Key.enter)
                    exp = str(x)+sign[z]+str(y) + "= " + str(ans)
                    keyboard.type("print(" + '"' + str(exp) + '"' + ")")
                    keyboard.press(Key.enter)
                    keyboard.release(Key.enter)
                    keyboard.press(Key.backspace)
                    keyboard.release(Key.backspace)
            else:
                ans = eval(str(x) + " " + sign[z] + " " + str(y))
                time.sleep(0.6)
                keyboard.type("if userinput1 == " + str(x) + " and sign == " + '"' + str(sign[z]) + '"' + " and userinput2 == " + str(y) +":")
                keyboard.press(Key.enter)
                keyboard.release(Key.enter)
                exp = str(x)+sign[z]+str(y) + "= " + str(ans)
                keyboard.type("print(" + '"' + str(exp) + '"' + ")")
                keyboard.press(Key.enter)
                keyboard.release(Key.enter)
                keyboard.press(Key.backspace)
                keyboard.release(Key.backspace)


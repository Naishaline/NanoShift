import serial
import pyautogui

ser = serial.Serial('COM8', 9600)
print(ser.name)
xVal = 0
yVal = 0
gear = 0
last_gear = 0

down_cutoff = 240

while True:
    try:
        if(ser.in_waiting > 0):
            serialString = str(ser.readline())[2:-5]
            split = serialString.split("|")
            xVal = int(split[0])
            yVal = int(split[1])
            if(yVal > down_cutoff and yVal < 620):
                gear = 0
            else:
                if(xVal < 400):
                    if(yVal < down_cutoff):
                        gear = 2
                    else:
                        gear = 1
                elif(xVal < 620):
                    if(yVal < down_cutoff):
                        gear = 4
                    else:
                        gear = 3
                else:
                    if(yVal < down_cutoff):
                        gear = 6
                    else:
                        gear = 5
            if(gear != last_gear):
                if(gear == 0):
                    pyautogui.press("g")
                elif(gear == 1):
                    pyautogui.press("h")
                elif(gear == 2):
                    pyautogui.press("j")
                elif(gear == 3):
                    pyautogui.press("k")
                elif(gear == 4):
                    pyautogui.press("l")
                elif(gear == 5):
                    pyautogui.press(";")
                elif(gear == 6):
                    pyautogui.press(".")
                print(gear)
                
            last_gear = gear
    except ValueError:
        print("Bad data, if you just ran the program don't worry.\nOtherwise... Something is whack, did a cable come loose?")
ser.close()
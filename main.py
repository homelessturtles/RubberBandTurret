import listener as listener
import serial# import serial library
import pyautogui as pg
import keyboard as key
import time
arduino = serial.Serial('/dev/cu.usbmodem141301', 9600)  # create serial object named arduino

def getxcoordinates():
    x, y = pg.position()
    newx = (180 - (x * 0.125))
    x = int(newx)
    servox = str(x)
    return servox

def getycoordinates():
    x,y = pg.position()
    newy = (180 - (y * 0.2002))
    y = int(newy)
    servoy = str(y)
    return servoy

def isbuttonpressed():
    if key.is_pressed('q'):
        return True
    else:
        return False

def shootangle():
    return '90'

def printcoordinates():
    if isbuttonpressed()==True:
        datastring = 'X' + getxcoordinates() + 'Y' + getycoordinates() + 'Z' + shootangle()
        return datastring
    else:
        datastring = 'X' + getxcoordinates() + 'Y' + getycoordinates() + 'Z180z'
        return datastring

while True:
    getxcoordinates()
    getycoordinates()
    isbuttonpressed()
    printcoordinates()

    arduino.write(printcoordinates().encode())
    time.sleep(0.025)
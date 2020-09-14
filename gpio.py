import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

def switch(color, mode):
    if color == 'red':
        pin = 21
    if color == 'yellow':
        pin = 19
    if color == 'green':
        pin = 23

    if mode == 'on':
        mode = 1
    if mode == 'off':
        mode = 0

    GPIO.setup(pin, GPIO.OUT, initial=mode)

def enableRed():
    switch('green', 'off')
    switch('yellow', 'off')
    switch('red', 'on')
    
def enableYellow():
    switch('green', 'off')
    switch('red', 'off')
    while True:
        switch('yellow', 'on')
        sleep(1)
        switch('yellow', 'off')
        sleep(1)

def enableGreen():
    switch('green', 'on')
    switch('yellow', 'off')
    switch('red', 'off')

enableYellow()
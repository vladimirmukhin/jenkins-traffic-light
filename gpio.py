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

while True:
    switch('red','on')
    switch('red','off')

def enableRed():
    switch('green', 'off')
    switch('yellow', 'off')
    switch('red', 'on')
    
def enableYellow():
    switch('green', 'off')
    switch('yellow', 'on')
    switch('red', 'off')

def enableGreen():
    switch('green', 'on')
    switch('yellow', 'off')
    switch('red', 'off')

While True:
    enableGreen()
    sleep(1)
    enableYellow()
    sleep(1)
    enableRed()
    sleep(1)
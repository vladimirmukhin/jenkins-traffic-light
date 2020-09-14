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
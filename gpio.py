import RPi.GPIO as GPIO
from time import sleep
import threading

GPIO.setmode(GPIO.BOARD)

def blink(color):
    while True:
        switch(color, 'on')
        sleep(1)
        switch(color, 'off')
        sleep(1)
        global stop_threads 
        if stop_threads: 
            break

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
    t1 = threading.Thread(target = blink('yellow')) 
    t1.start()

def enableGreen():
    switch('green', 'on')
    switch('yellow', 'off')
    switch('red', 'off')

stop_threads = False
enableYellow()
time.sleep(10) 
stop_threads = True
t1.join() 

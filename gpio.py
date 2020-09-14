import RPi.GPIO as GPIO
from time import sleep
import threading

GPIO.setmode(GPIO.BOARD)

class myThread (threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
   def run(self):
      blink('yellow')

def blink(color):
    while True:
        switch('yellow', 'on')
        sleep(1)
        switch('yellow', 'off')
        sleep(1)
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
    thread1 = myThread(1, "Thread-1", 1)
    thread1.start()
    sleep(10)
    stop_threads = True

def enableGreen():
    switch('green', 'on')
    switch('yellow', 'off')
    switch('red', 'off')

enableYellow()
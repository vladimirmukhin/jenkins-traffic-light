#!/usr/bin/python3

import jenkins
from termcolor import colored, cprint
from time import sleep
from os import getenv
import RPi.GPIO as GPIO
import multiprocessing

jenkins_url      = getenv('JENKINS_URL')
jenkins_username = getenv('JENKINS_USERNAME')
jenkins_password = getenv('JENKINS_PASSWORD')

server = jenkins.Jenkins(jenkins_url, username=jenkins_username, password=jenkins_password)

while (True):
    job_info = server.get_job_info('store-dev')
    build_info = server.get_build_info('store-dev', job_info["lastBuild"]["number"])
    proc = multiprocessing.Process(target=enableYellow, args=())

    if build_info['building'] == True:
        color = 'yellow'
        build_info['result'] = 'IN PROGRESS'
        #blink yellow
        proc.start()
    elif build_info['result'] == 'SUCCESS':
        color = 'green'
        proc.terminate()
        enableGreen()
    elif build_info['result'] == 'FAILURE':
        color = 'red'
        proc.terminate()
        enableRed()
    elif build_info['result'] == 'ABORTED':
        color = red
        proc.terminate()
        enableRed()

    print('\033c')
    print(colored(build_info['result'], color))
    
    sleep(4)

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
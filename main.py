#!/usr/bin/python3

import jenkins
from termcolor import colored, cprint
from time import sleep
from os import getenv
import RPi.GPIO as GPIO

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

jenkins_url      = getenv('JENKINS_URL')
jenkins_username = getenv('JENKINS_USERNAME')
jenkins_password = getenv('JENKINS_PASSWORD')

GPIO.setmode(GPIO.BOARD)

server = jenkins.Jenkins(jenkins_url, username=jenkins_username, password=jenkins_password)

while (True):
    job_info = server.get_job_info('store-dev')
    build_info = server.get_build_info('store-dev', job_info["lastBuild"]["number"])

    if build_info['building'] == True:
        color = 'yellow'
        build_info['result'] = 'IN PROGRESS'
    elif build_info['result'] == 'SUCCESS':
        color = 'green'
    elif build_info['result'] == 'FAILURE':
        color = 'red'
    elif build_info['result'] == 'ABORTED':
        color = 'red'

    #display current status in terminal
    print('\033c')
    print(colored(build_info['result'], color))

    #reset traffic light colors
    switch('red', 'off')
    switch('green', 'off')
    switch('yellow', 'off')

    #enable required color
    switch(color,'on')

    sleep(4)

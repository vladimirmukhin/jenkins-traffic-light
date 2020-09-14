#!/usr/bin/python3

import jenkins
from termcolor import colored, cprint
from time import sleep

server = jenkins.Jenkins('http://localhost:8080', username='admin', password='123456')

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
        color = 'yellow'

    print('\033c')
    print(colored(build_info['result'], color))
    
    sleep(4)
#!/usr/bin/env python

from subprocess import Popen
from gpio_utils import setup


PATH = "/home/pi/raspdoor/"

def main ():
    processes = [PATH + 'call_service.py', PATH + 'rfid_service.py']
    for process in processes:
        Popen(process)

if __name__ == '__main__':
    # setup()
    main()

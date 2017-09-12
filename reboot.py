import socket
import requests
from datetime import datetime


details = []

# kiolvassuk a bejelentkezesi adatokat a routerhez
with open('/home/default/Documents/rebooter/details.dat') as f:
    for line in f:
        details.append(line.strip())

# megnezzuk az aktualis IP cimunket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ip = s.getsockname()[0]

with open('/home/default/Documents/rebooter/reboot-log.dat', 'a') as f:
    if not ip.startswith("152.66"):
        # ha nem publikus az IP, inditsuk ujra a routert
        try:
            r = requests.get('http://192.168.0.1/Reboot.asp', auth=(details[0], details[1]))
            f.write("{} {}\n".format(str(datetime.now()), r.status_code))
        except requests.exceptions.ConnectionError:
            f.write("{} exception\n".format(str(datetime.now())))

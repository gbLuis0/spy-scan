from socket import socket, AF_INET, SOCK_STREAM
from os import system, name
try:
    from pyfiglet import Figlet
except:
    system('pip install pyfiglet -y')
finally:
    from pyfiglet import Figlet

banner = Figlet(font='slant').renderText('Spy-scan')

def cls():
    system("cls" if name == 'nt' else "clear")

portas = [20, 21, 22, 23, 25, 53, 80, 118, 119, 135, 143, 443, 3306, 8080]
az = '\033[34;1m'
f = '\033[m'
n = '\033[1m'
per = 'y'

while per == 'y':
    cls()
    print(banner)
    host = input(n+'Digite IP ou domínio: ').strip().lower()
    print('Port ', ' Situation\n-----------------')
    for p in portas:
        con = socket(AF_INET, SOCK_STREAM)
        con.settimeout(0.45)
        rsp = con.connect_ex((host, p))
        print(f'{az}{p:<7} \033[32;1mOPEN{f}' if rsp == 0 else f'{az}{p:<7} \033[31;1mCLOSED{f}')
    per = input(f'{n}Deseja realizar outro scan? [{az}y{f}/{az}n{f}] ').strip().lower()[0]
cls()

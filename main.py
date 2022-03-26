from os import system, name
import argparse
from sys import argv
from socket import socket, AF_INET, SOCK_STREAM

portas = [20, 21, 22, 23, 25, 53, 80, 118, 119, 135, 143, 443, 3306, 8080]
time = 0.4
n = '\033[1m'
az = '\033[34;1m'
f = '\033[m'

parser = argparse.ArgumentParser(
    description="Um Port Scanner; by: spyware",
    usage=f'{argv[0]} -d HOST')

parser.add_argument(
    '-d', '--host',
    help="Host que será escaneado"
)

parser.add_argument(
    '-n', '--nivelscan', type=int, metavar='1 or 2',
    help='Portas para escanear; 1: principais portas; 2: todas as portas (65.536) (opcional)'
)

parser.add_argument(
    '-t', '--time', type=float,
    help='Tempo para escaneamento (segundos) (opcional)'
)

opt = {1: portas, 2: list(range(65536))}

args = parser.parse_args()
if args.nivelscan:
    portas = opt[args.nivelscan]

if args.time:
    time = args.time

system('cls' if name == 'nt' else 'clear')
if len(argv) <= 1:
    parser.print_help()
    exit(0)

if args.host:
    print(f'Scanning {n}{args.host}{f}...')
    print('Port  ', '  Situation\n-------------------')
    for p in portas:
        con = socket(AF_INET, SOCK_STREAM)
        con.settimeout(time)
        rsp = con.connect_ex((args.host, p))
        con.close()
        if rsp == 0:
            print(f'{az}{p:<9} \033[32;1mOPEN{f}'+' '*50)
        else:
            print(f'{az}{p:<9} \033[31;1mCLOSED{f}'+' '*50, end='\r')

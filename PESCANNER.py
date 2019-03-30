#!/usr/bin/python3
import sys
import requests
import argparse

from core.hq import hq
from core.extractor import extractor
from core.colors import white, green, end, red, yellow, run

parser = argparse.ArgumentParser()
parser.add_argument('-t', help='you know what this is ;)', dest='target')
parser.add_argument('-c', help='pick a choice to choose from! ', dest='choice')
parser.add_argument('--domains', help='basically the domain :3', dest='domains', action='store_true')
parser.add_argument('--ips', help='TRACE IP, SCAN IP, EPIC HAXORRR', dest='ips', action='store_true')
args = parser.parse_args()

ips = args.ips
target = args.target
choice = args.choice
domains = args.domains

data = False
if ips or domains:
    data = sys.stdin.readlines()

arged = False
if target and choice:
    arged = True

if sys.version_info < (3, 0):
    input = raw_input


def banner():
    print ('''%s
  _____ %s ______%s  _____  _____          _   _ _   _ ______ _____  
 |  __ \%s|  ____%s |/ ____|/ ____|   /\   | \ | | \ | |  ____|  __ \ 
 | |__) %s| |__  %s | (___ | |       /  \  |  \| |  \| | |__  | |__) |
 |  ___/%s|  __| %s  \___ \| |      / /\ \ | . ` | . ` |  __| |  _  / 
 | |    %s| |____%s  ____) | |____ / ____ \| |\  | |\  | |____| | \ \ 
 |_|    %s|______%s |_____/ \_____/_/    \_\_| \_|_| \_|______|_|  \_\ v101 idfk%s''' % (white, red, white, red, white, red, white, red, white, red, white, red, white, end))


def menu():
    print('''
%s1.%s Censys scannorrr
%s2.%s DNS lookup
%s3.%s Port scannorrr
%s4.%s CMS Scannorrr
%s5.%s Whois lookup
%s6.%s honeypot scannorrr
%s7.%s subdomains scannorrr
%s8.%s Reverse IP lookup
%s9.%s technologies or IoT scannorrr
%s0.%s All''' % (white, end, white, end, white, end, white, end, white, end, white, end, white, end, white, end, white, end, white, end))


def PESCANNER(choice, target):
    if not args.target:
        banner()
    if arged:
        hq(choice, target)
    else:
        while True:
            menu()
            result = False
            choice = input('\033[1;91moofboii->\033[0m ')
            hq(choice)


if data:
    kind = 'domain'
    if ips:
        kind = 'ip'
    targets = extractor(data, kind)
    if choice:
        for target in targets:
            print ('%s %s' % (run, target))
            hq(choice, target)
            print (red + ('-' * 60) + end)
    else:
        for target in targets:
            sys.stdout.write(target + '\n')
else:
    try:
        PESCANNER(choice, target)
    except KeyboardInterrupt:
        quit('')

import re
import os
import sys
import math

from enum import Enum

class Platform(Enum):
    LINUX = 0
    MACOS = 1
    WINDOWS = 2

if sys.platform == "linux" or sys.platform == "linux2":
    platform = Platform.LINUX
    RE_PING_SPEED = re.compile(r'=\s*(\d+\.?\d*)/')
    PING_CMD = 'ping -c 1 -w {wait} {ip}'
elif sys.platform == "darwin":
    platform = Platform.MACOS
    RE_PING_SPEED = re.compile(r'=\s*(\d+\.?\d*)/')
    PING_CMD = 'ping -c 1 -W {wait} {ip}'
elif sys.platform == "win32":
    platform = Platform.WINDOWS
    RE_PING_SPEED = re.compile(r'=(\d+)ms')
    PING_CMD = 'ping /n 1 /w {wait} {ip}'
else:
    raise Exception('Unkown OS')

def ping_time(ip, wait=100):
    if platform == Platform.LINUX:
        wait = math.ceil(wait / 1000) # seconds
    cmd_out = os.popen(PING_CMD.format(ip=ip, wait=wait)).read()
    match = RE_PING_SPEED.search(cmd_out)
    try:
        spend = match.group(1)
        return math.ceil(float(spend))
    except:
        return 0

def filter_and_sort(ip_list, wait=100, save_to=None):
    ip_time_dict = {}
    if save_to:
        with open(save_to, 'w') as file:
            file.write('ip,ms\n')
    for ip in ip_list:
        if ip in ip_time_dict:
            continue
        spend = ping_time(ip, wait)
        if save_to:
            with open(save_to, 'a') as file:
                file.write('{},{}\n'.format(ip, spend))
        if spend > 0:
            ip_time_dict[ip] = spend
    if not ip_time_dict:
        return []
    sorted_ip_list = sorted(ip_time_dict, key=ip_time_dict.get)
    return sorted_ip_list

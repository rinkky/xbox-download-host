import re
import os
import math

if os.name == 'posix':
    RE_PING_SPEED = re.compile(r'=\s*(\d+\.?\d*)/')
    PING_CMD = 'ping -c 1 -W {wait} {ip}'
else:
    RE_PING_SPEED = re.compile(r'=(\d+)ms')
    PING_CMD = 'ping /n 1 /w {wait} {ip}'

def ping_time(ip, wait=100):
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

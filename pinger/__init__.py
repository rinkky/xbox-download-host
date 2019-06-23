import re
import os

RE_PING_SPEED = re.compile(r'=(\d+)ms')

def ping_test(ip, wait=50):
    cmd_out = os.popen(
        'ping /n 1 /w {wait} {ip}'.format(ip=ip, wait=wait)
    ).read()
    return not ('100%' in cmd_out)

def ping_time(ip, wait=50):
    cmd_out = os.popen('ping /n 1 /w {wait} {ip}'.format(
        ip=ip, wait=wait
    )).read()
    match = RE_PING_SPEED.search(cmd_out)
    try:
        spend = match.group(1)
        return int(spend)
    except:
        return 0

def filter_and_sort(ip_list, wait=50, save_to=None):
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

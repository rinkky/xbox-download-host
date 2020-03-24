import os
import time
import pinger
import xbox

ip_list_file = 'data/ip.list'
log_folder = 'log'
hosts_file = '{}/hosts.txt'.format(log_folder)
download_speed_log_file = '{}/speed.log'.format(log_folder)
ping_log_file = '{}/ping.log'.format(log_folder)

def main():
    ## init
    if not os.path.exists(log_folder):
        os.makedirs(log_folder)
    with open(ip_list_file, 'r') as file:
        raw = file.read()
    with open(hosts_file, 'w') as file:
        file.write('###########{}###########\n\n'.format(time.ctime()))
    with open(download_speed_log_file, 'w') as file:
        file.write('###########{}###########\n\n'.format(time.ctime()))
    ip_list = raw.split()
    
    ## filter ip list
    print('filter ip list...')
    sorted_ip = pinger.filter_and_sort(ip_list, 50, save_to=ping_log_file)
    if not sorted_ip:
        print('error: no available ip in list')
        return None
    
    ## check download speed
    print('start checking download speed')
    ip_cnt = min(50, len(sorted_ip))
    ip_speed_dict = {}
    for i in range(ip_cnt):
        ip = sorted_ip[i]
        if ip in ip_speed_dict:
            continue
        print('{} checking...'.format(ip))
        speed = xbox.download_speed(ip)
        print('{} MB/s\n------------'.format(speed))
        with open(download_speed_log_file, 'a') as file:
            file.write('{}\t{} MB/s\n'.format(ip, speed))
        ip_speed_dict[ip] = speed
    
    ## find fastest hosts
    sorted_ip = sorted(ip_speed_dict, key=ip_speed_dict.get, reverse=True)
    with open(hosts_file, 'a') as file:
        file.write('{}    assets1.xboxlive.com\n'.format(sorted_ip[0]))
        index = min(1, len(sorted_ip) - 1)
        file.write('{}    assets2.xboxlive.com\n'.format(sorted_ip[index]))
    
    ## done
    print('All done.\nDownload speed log: {}\nFastest host: {}\n'.format(
        download_speed_log_file, hosts_file
    ))

if __name__ == "__main__":
    main()

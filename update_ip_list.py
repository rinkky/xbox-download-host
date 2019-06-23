import re
import time
import requests

from bs4 import BeautifulSoup

re_ip = re.compile(r'\d+\.\d+\.\d+\.\d+$')
domain_list = ['download.xboxlive.com', 'assets1.xboxlive.com', 'assets2.xboxlive.com']
ip_list_file = 'data/ip.list'

def get_ip_list_of(domain):
    ip_list = []
    url = 'http://site.ip138.com/{}/'.format(domain)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    curadress_tag = soup.find(id='curadress')
    for tag in curadress_tag.next_siblings:
        if tag.name == 'p':
            ip = _get_ip_from_a(tag.a)
            if ip:
                ip_list.append(ip)
    return ip_list

def _get_ip_from_a(a):
    if not a.string:
        return ''
    a_string = a.string.strip()
    match = re_ip.match(a_string)
    if(match is None):
        return ''
    return a_string

def main():
    ip_list = []
    for domain in domain_list:
        ip_list.extend(get_ip_list_of(domain))
        time.sleep(1)
    ip_list = list(set(ip_list))
    with open(ip_list_file, 'w') as file:
        file.write('\n'.join(ip_list))

if __name__ == "__main__":
    print('updating ip list...')
    main()
    print('update success. ip list file: {}'.format(ip_list_file))

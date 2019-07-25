import os

curl_cmd = 'curl'
url_postfix='/5/795514b6-aad9-4c1c-ac2a-60c1492d7f31/0c57204f-f4f0-4bf6-b119-b7afc231994d/0.0.61375.0.6574fcb5-72f2-4c85-98c1-bd1059c79934/Destiny2_0.0.61375.0_neutral__z7wx9v9k22rmg'
curl_range='33543139328-33752035327'

def download_speed(ip):
    """MB/s"""
    cmd = '{curl} -s -o nul -m 10 -r {range} -y 5 --url "http://{ip}{url_postfix}" -H "Host: assets1.xboxlive.com" -w "{curl_w}"'
    cmd = cmd.format(
        curl=curl_cmd,
        range=curl_range,
        ip=ip,
        url_postfix=url_postfix,
        curl_w='%{speed_download}'
    )
    cmd_out = os.popen(cmd).read()
    if os.path.exists('nul'):
        os.remove('nul')
    return round(float(cmd_out)/1024/1024, 2)

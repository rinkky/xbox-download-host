import time
import requests

curl_cmd = 'curl'
url_postfix='/5/795514b6-aad9-4c1c-ac2a-60c1492d7f31/0c57204f-f4f0-4bf6-b119-b7afc231994d/0.0.61375.0.6574fcb5-72f2-4c85-98c1-bd1059c79934/Destiny2_0.0.61375.0_neutral__z7wx9v9k22rmg'
curl_range='33543139328-33574596608'

def download_speed(ip):
    """
    returns MB/s
    """
    url = 'http://{}{}'.format(ip, url_postfix)
    headers = {'Host': 'assets1.xboxlive.com', 'range': curl_range}
    dl = 0
    try:
        rsp = requests.get(url, headers=headers, stream=True, timeout=4)
        start = time.clock()
        for chunk in rsp.iter_content(1024):
            dl += 1024
            if time.clock() - start > 5:
                break
    except Exception:
        pass
    time_used = time.clock() - start
    return round(dl / time_used / 1024 / 1024, 2)

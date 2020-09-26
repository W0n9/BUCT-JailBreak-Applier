# %%
import requests
from bs4 import BeautifulSoup
from typing import Mapping

url = 'http://wx.buct.edu.cn/qiyehao/baoweichu1/linshi2/create_baobei.php?y=2'

if __name__ == "__main__":
    s = requests.session()
    headers: Mapping[str, str] = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36 QBCore/4.0.1301.400 QQBrowser/9.0.2524.400 Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2875.116 Safari/537.36 NetType/WIFI MicroMessenger/7.0.5 WindowsWechat'
    }
    cookies: Mapping[str, str] = {'PHPSESSID': ''}  # 抓包获取Session
    payload: Mapping[str, str or int] = {
        'name': '',  # 姓名
        'gh': '',  # 学号
        'bumen': '',  # 学院名称(Optional)
        'ssl': '',  # 校区名称(Optional)
        'cfd': '',  # 去往目的地(Optional)
        'gj': ''  # 出校原因(Optional)
    }

    result = s.post(url, data=payload, cookies=cookies, headers=headers)
    if result.status_code == 200:
        soup = BeautifulSoup(result.text, 'html.parser')
        print(soup.h2.contents)

# %%

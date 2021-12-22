from webvpn import WebVPN
import re

user = ''
pasw = ''

vpn = WebVPN()
vpn.login(user, pasw)
vpn.get('http://eamis.nankai.edu.cn/eams/homeExt.action')
w = vpn.get(
    'http://eamis.nankai.edu.cn/eams/stdDetail!innerIndex.action?projectId=1')
p = re.compile('姓名：</td>.*?<td>(.+?)</td>', re.S)
name = p.findall(w.content.decode('UTF-8'))
if name:
    print('你好，', name[0])

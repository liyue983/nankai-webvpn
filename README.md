# 登录到南开大学 webvpn

通过该模块可以登录到南开大学的 [webvpn](https://webvpn.nankai.edu.cn/)，以便使用校园网代理进行页面访问。

[程序使用示例](example.py)：

```python
from webvpn import Webvpn
import re

user = ''
pasw = ''

vpn = Webvpn()
vpn.login(user,pasw)
vpn.get('http://eamis.nankai.edu.cn/eams/homeExt.action')
w = vpn.get('http://eamis.nankai.edu.cn/eams/stdDetail!innerIndex.action?projectId=1')
p = re.compile('姓名：</td>.*?<td>(.+?)</td>',re.S)
name = p.findall(w.content.decode('UTF-8'))
if name:
    print('你好，',name[0])
```

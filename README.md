# 登录到南开大学 webvpn

通过该模块可以登录到南开大学 [webvpn](https://webvpn.nankai.edu.cn/)，同时可以利用 webvpn 访问一些校内网站。

使用前确保有 pycryptodome 和 requests 这两个库，可以通过下面的命令安装

```shell
pip install -r requirements.txt
```

[示例](example.py)：

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

`vpn.login()`用于登录到 webvpn

`vpn.get()`发起 get 请求，可以传入的参数与 requests.get() 一致，比如 headers，params 等

其他还有`vpn.post()`和`vpn.request()`，使用方法和 requests 一致。

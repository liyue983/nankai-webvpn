import re
from Crypto.Cipher import AES

wrdvpnKey = 'wrdvpnisthebest!'
wrdvpnIV = 'wrdvpnisthebest!'


def encrypUrl(protocol, url):
    port = ""
    segments = ""

    if url[:7] == "http://":
        url = url[7:]
    elif url[:8] == "https://":
        url = url[8:]

    v6 = ""
    match = re.compile("/\[[0-9a-fA-F:]+?\]/").match(url)
    if match:
        v6 = match[0]
        url = url[len(match[0]):]
    segments = url.split("?")[0].split(":")
    if len(segments) > 1:
        port = segments[1].split("/")[0]
        url = url[0:len(segments[0])] + url[len(segments[0]) + len(port) + 1:]

    if protocol != "connection":
        i = url.find('/')
        if i == -1:
            if v6 != "":
                url = v6
            url = encrypt(url, wrdvpnKey, wrdvpnIV)
        else:
            host = url[:i]
            path = url[i:]
            if v6 != "":
                host = v6
            url = encrypt(host, wrdvpnKey, wrdvpnIV) + path
    if port != "":
        url = "/" + protocol + "-" + port + "/" + url
    else:
        url = "/" + protocol + "/" + url
    return url


def encrypt(text, key, iv):
    textLength = len(text)
    text = textRightAppend(text, 'utf8')
    keyBytes = key.encode(encoding='UTF-8')
    ivBytes = iv.encode(encoding='UTF-8')
    textBytes = text.encode(encoding='UTF-8')
    aesCfb = AES.new(keyBytes, AES.MODE_CFB, ivBytes, segment_size=128)
    encryptBytes = aesCfb.encrypt(textBytes)
    return ivBytes.hex() + encryptBytes.hex()[:textLength * 2]


def textRightAppend(text, mode):
    segmentByteSize = 16 if mode == 'utf8' else 32
    if len(text) % segmentByteSize == 0:
        return text
    appendLength = segmentByteSize - len(text) % segmentByteSize
    text += '0' * appendLength
    return text

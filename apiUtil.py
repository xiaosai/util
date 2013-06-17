#coding=utf-8
import urllib2
import urllib
import datetime
import hmac
import binascii
from hashlib import sha1
from urlparse import urlparse

# 签名请求规范 http://wiki.sankuai.com/pages/viewpage.action?pageId=29755412
class httpClient:
    # 时间格式 Wed, 27 Mar 2013 07:44:22 GMT
    GMT_FORMAT = '%a, %d %b %Y %H:%M:%S GMT'

    def getAuthorization(self, uri, method, client_id, secret, date):
        date_str = date.strftime(self.GMT_FORMAT)
        key = secret 
        # GET/POST + " " + uri + "\n" + time  
        string_to_sign = method + " " + uri + "\n" + date_str
        # sha 算法加密
        hashed = hmac.new(secret, string_to_sign, sha1)
        # The signature, 使用base64
        signature = binascii.b2a_base64(hashed.digest())[:-1]
        authorization = "MWS" + " " + client_id + ":" + signature
        return authorization

    def get(self, url, client_id = '', secret = ''):
        #utc 时间
        date = datetime.datetime.utcnow()
        uri = urlparse(url).path
        request = urllib2.Request(url)
        if client_id != '':
            authorization = self.getAuthorization(uri, "GET", client_id, secret, date)
            request.add_header('Authorization', authorization) 
            request.add_header('Date', date.strftime(self.GMT_FORMAT)) 
            print authorization
            print date.strftime(self.GMT_FORMAT)
        response = urllib2.urlopen(request)
        print response.read()


    def post(self, url, data, client_id = '', secret = ''):
        #utc 时间
        date = datetime.datetime.utcnow()
        uri = urlparse(url).path
        request = urllib2.Request(url)
        # 判断是否需要ba验证
        if client_id != '': 
            authorization = self.getAuthorization(uri, "POST", client_id, secret, date)
            # 设置验证
            request.add_header('Authorization', authorization) 
            request.add_header('Date', date.strftime(self.GMT_FORMAT)) 
            print authorization
            print date.strftime(self.GMT_FORMAT)
        # 填入数据
        request.add_data(urllib.urlencode(data))
        response = urllib2.urlopen(request)
        return response.read() 

if __name__ == '__main__':
    client = httpClient()
    url = 'http://open.cjkmt.dev.sankuai.com/biz/19520'
    client.get(url, 'card', '1bbe678721426fb5cf3f2b1a35307959')

    #url = 'http://release.crm.test.sankuai.info/api/account/search?poiIds=897649,897650'
    #client.get(url, 'contract', '23b4ef8b728d1aced0d73e8794e2c63b')
    #url = 'http://localhost:8080/api/contract?contractIds=ffe8dbf6-913c-11e2-9b3c-00222822153f'


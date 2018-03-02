# encoding: utf-8

import urllib
import urllib2
import json
import httplib


def http_post(url, params, cookie=None):
    """
    发去post的请求，得到返回结果
    :param url:
    :param params:
    :param cookie:
    :return:
    """
    try:
        req = None
        values = urllib.urlencode(params)
        if cookie is not None or cookie == "":
            req = urllib2.Request(url, values, headers={'Cookie': cookie})
        else:
            req = urllib2.Request(url, values)
        response = urllib2.urlopen(req)
        return json.loads(response.read())
    except urllib2.HTTPError,e:
        # print e.code
        return json.loads(e.read())
    except urllib2.URLError, e:
        return "URL地址:%s 有误，找不到服务器～" % url


def http_get(url, params=None, cookie=None):
    """
    发起get请求，得到返回结果
    :param url:
    :param params:
    :param cookie:
    :return:
    """
    try:
        req_url = url
        req = None
        if params is not None or cookie == "":
            values = urllib.urlencode(params)
            req_url = url + "?" + values
        if cookie is not None:
            req = urllib2.Request(req_url, headers={'Cookie': cookie})
        else: req = urllib2.Request(req_url)
        response = urllib2.urlopen(req)
        return json.loads(response.read())
    except urllib2.HTTPError, e:
        # print e.code
        return json.loads(e.read())
    except urllib2.URLError, e:
        return "接口的服务器地址%s错误，找不到服务器～" % url


def __http_get(url, params,cookie):
    req_url = url
    if params is not None:
        values = urllib.urlencode(params)
        req_url = url + "?" + values
    conn = httplib.HTTPConnection("ucapi.jumeicd.com")
    conn.request(method='GET', url=req_url, headers={'Cookie': cookie})
    response = conn.getresponse()
    res = json.loads(response.read())
    # print res
    # print res.get("message")
    return res


if __name__ == "__main__":
    # print http_post("http://ucapi.jumeicd.com/Order/Detail",{"client_v":4.5,"platform":"Android","site":"www"})
    cookie_str = "default_site_25=bj; language=zh; source=oppo; imsi=460013687600774; resolution=720*1200; register_time=1488262981; mac=860793037643979; platform=android; operator=ChinaUnicom; network=wifi; uid=2000030415; cookie_ver=1; httpDnsVersion=31; userTagId=8; httpDnsCase=0; nickname=luoranbin36; PHPSESSID=3d16f5a57812438a2e51f12ce3367ba0; unique_device_id=VKQd4CnC3IADANwb3KTZKCJ7; model=OPPO A53m; install_source=C_000; brand=OPPO; user_ip=172.20.80.253; ab=144:b|164:v8|166:b|180:hide|182:b|183:b|203:show|281:v3|667:fake|701:show|802:show|901:show|1001:C|1655:v8|73159:new|73162:e|100101:2b; product=jumei; device_id=df04fe465e8bafccdf32ede2a6126fc7; user_tag_id=8; uc_api_session_id=594b595eaf6aa2266; client_v=4.556; privilege_group=2; postcode=110000; v_uid=2000030415; platform_v=5.1.1; appfirstinstall=0; site=bj; device_uid=125a51e1-ca30-415c-b4d9-1acecf353116; referer_site=app_android_com.jm.android.jumei_oppo_v4.556_bj; tk=933f82be949ddf294712a76d13609994b334a0f5; appid=com.jm.android.jumei; appsecret=114ab1fa; containercontent=1.1.0; imei=860793037643979; account=9ttORYrX2Kg5HzMsHHs1j75RrQisd3cx5ai%2FTHhZhgfDyrcBQE%2F4gGzGaAS7inAZH4vopAosqMuShaVpZUCToMX0WdYiYAJbXHxnXc39rEiCBVJ2QkyFcPfQkCrMCzDU1uiifLAx0SjVDDU7i95sh3Cy3u2UnTL91%2FmJz5NSICJ85v80RCNpwOZGzybLGOXjNWcA2l7UZuLOoKlFYYYSEg%3D%3D; is_first_open=0; hybridcontainer=173"
    # aa= http_get("http://ucapi.jumeicd.com/v2/Order/List",{"client_v":"4.5","platform":"Android","site":"bj","page":1,"limit":20},cookie_str)
    # print aa
    # print aa.get("message")phone6490
    # cookie_str=""
    aa=http_post("http://passport.api.jumeicd.com/v1/Login/Password",{"client_v":3.848,"platform":"Android","site":"www","username":"mett","password":"ossLbHoQxvI=","sdk_reg_id":"6d29cddafa592035926d841af5ff5e3c","sdk_vendor":"GTPush","platform_model":"OPPO A53m","platform_brand":"OPPO","platform_type":"phone"})
    print aa
    print aa.get("message")
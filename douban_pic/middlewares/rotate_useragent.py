# -*-coding:utf-8-*-  
  
import logging
import random

from scrapy.contrib.downloadermiddleware.useragent import UserAgentMiddleware


class RotateUserAgentMiddleware(UserAgentMiddleware):  
  
    def __init__(self, user_agent=''):  
        self.user_agent = user_agent  
  
    def process_request(self, request, spider):  
        ua = random.choice(self.user_agent_list)  
        if ua:
            logging.log(logging.INFO, 'Current UserAgent: '+str(ua))  
            request.headers.setdefault('User-Agent', ua)  
  
    #the default user_agent_list composes chrome,I E,firefox,Mozilla,opera,netscape  
    #for more user agent strings,you can find it in http://www.useragentstring.com/pages/useragentstring.php  
    user_agent_list = [ 
        """Connection: keep-alive
Accept: application/json, text/javascript, */*; q=0.01
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36
Referer: https://www.douban.com/
Accept-Encoding: gzip, deflate, sdch, br
Accept-Language: zh-CN,zh;q=0.8,en;q=0.6,pt;q=0.4,zh-TW;q=0.2,ja;q=0.2
Cookie: bid="ixZa/ik+ac"; gr_user_id=76eb30fb-8455-4022-ad5f-b1a31ba2d7b; ll="108288"; viewed="26312313_26301966_1148259_1246297_4088039_1881631_3729216_5383553_6021440"; ps=y; ct=y; _ga=GA1.2.812824216.1443974968; ue="258789822@qq.com"; dbcl2="57615954:FzEwVhjgnI"; ck=lOpV; _vwo_uuid_v2=81A6692CD34284D5D6BC1CF682894B58|e01325a009433e97bd1eb032b47e3117; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1472122206%2C%22https%3A%2F%2Faccounts.douban.com%2Flogin%22%5D; _pk_id.100001.8cb4=c0ab39ce68baa90b.1443974968.31.1472122206.1472120024.; _pk_ses.100001.8cb4=*; push_noty_num=0; push_doumail_num=0; __utmt=1; __utma=30149280.812824216.1443974968.1472120007.1472122206.49; __utmb=30149280.2.10.1472122206; __utmc=30149280; __utmz=30149280.1472120007.48.36.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/login; __utmv=30149280.5761; ap=1","""
       ]  

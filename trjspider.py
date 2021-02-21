# -*- coding = utf-8 -*-
# @Time :2021-02-21 14:44
# @Author: YanXia
# @File : trjspider.py
# @Software: PyCharm
import requests,time
from lxml import etree
headers = {'content-type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}
def tiqu():
  print("""
  _  __          _  __
 | |/,'_   _    | |/,'() _
 | ,','o| / \/7 /  / /7,'o|
/_/  |_,7/_n_/,'_n_\// |_,7
                  QQ:210246020         
                          """)          
 for page in range(0,220,20):
  try:
   url='https://movie.douban.com/subject/27619748/comments?start=%d&limit=20&status=P&sort=new_score'%page
   r = requests.get(url,headers=headers,timeout=1).content.decode('utf-8')
   soup = etree.HTML(r)
   tiqu=soup.xpath('//p[@class=" comment-content"]/span[@class="short"]/text()')
   print(tiqu)
   tiqu='\n'.join(tiqu)
   with open(r'trj1.txt', 'a+',encoding='UTF-8') as f:
      f.write(tiqu + '\n')
      f.close()
   time.sleep(1)
  except Exception as e:
   pass

if __name__ == '__main__':
    tiqu()

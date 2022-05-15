# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import requests
import json
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
   url='URL:https://movie.douban.com/j/chart/top_list'
   param={
       'type':'24',
       'interval_id':'100:90',
       'action':'',
       'start':'1',
       'limit':'20'
   }
   headers={
       "User - Agent": "Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 101.0.4951 .64Safari / 537.36Edg / 101.0.1210.47"
   }
   response=requests.get(url=url,params=param,headers=headers)
   list_data=response.text
   fp=open('./douban.text','w',encoding='utf-8')
   json.dump(list_data,fp=fp,ensure_ascii=False)
   print("over!")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

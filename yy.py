# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import requests
import json
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
   url='https://www.sogou.com/'
   headers={
       "User - Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.47"
   }
   response=requests.get(url=url,headers=headers)
   list_data=response.text
   fp=open('./sougou.html','w',encoding='utf-8')
   fp.write(list_data)
   print("over!")
import requests
from lxml import etree
if __name__ == '__main__':
    url="https://movie.douban.com/cinema/nowplaying/changsha/"
    headers={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.47"}
    page_text=requests.get(url=url,headers=headers).text
    # //xpath解析定位
    tree=etree.HTML(page_text)
    li_list=tree.xpath("//li[@class='stitle']")
    fp = open('./ershoufang.txt', 'w', encoding='utf-8')
    for li in li_list:
        title=li.xpath("./a/text()")[0]
        fp.write(title)
    print("over!")
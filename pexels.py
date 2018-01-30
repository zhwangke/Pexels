# -*- coding:utf8 -*-
# Version : Python3.6
# Date : 2018/01/29
"""
功能：爬取www.pexels.com的美图

"""
import requests
import re
import os
from hashlib import md5
from urllib.parse import urlencode

def getHtml():
    """
    首先分析网页获取单页的html文件

    """
    for page in range(start_url, end_url+1):
        data = {"page":page}
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                          " Chrome/61.0.3163.100 Safari/537.36"
            }
        base = urlencode(data)
        url = 'https://www.pexels.com/?format=js&' + base
        response = requests.get(url,headers=headers)
        html = response.text
        #return html
        getUrl(html,page)
def getUrl(html,page):

    """

    根据获取的html文件提取图片的下载链接

    """
    pattern = re.compile('(https://images.*?(jpeg|jpg|png))', re.S)
    imglist = re.findall(pattern, html)
    piclist = list(set(imglist))
    # print(piclist)
    for img in piclist:
        pic = img[0]
        #print(pic)
        writeFile(pic)
    if page == start_url:
   	print("第{}页下载完成...".format(page) + "\n")
	print("开始下载第{}页...".format(page+1))
    else:
	print("第{}页下载完成...".format(page) + "\n")
	print("任务完成，Thank you !!!")

def writeFile(pic):
    """
    把所有的图片保存到本地

    """
    print("正在下载" + pic)
    content = requests.get(pic).content
    #md5随机作为文件名，防止程序中断重复下载
    filename = '{}/{}.{}'.format(os.getcwd(),md5(content).hexdigest(),'jpeg')
    with open(filename,'wb') as f:
        f.write(content)

if __name__ == '__main__':
    start_url = int(input("请输入需要下载的开始页："))
    end_url = int(input("请输入需要下载的结束页："))
    print("\n" + "图片都是高清大图，正在努力加载，请稍等...")
    getHtml()


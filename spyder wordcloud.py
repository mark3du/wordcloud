# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 16:55:55 2019

@author: 杜敬祎
"""

import urllib.request
from bs4 import BeautifulSoup


def getHtml(url):
    """获取url页面"""
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
    req = urllib.request.Request(url,headers=headers)
    req = urllib.request.urlopen(req)
    content = req.read().decode('utf-8')

    return content


def getComment(url):
    """解析HTML页面"""
    html = getHtml(url)
    soupComment = BeautifulSoup(html, 'html.parser')

    comments = soupComment.findAll('span', 'short')
    onePageComments = []
    for comment in comments:
        # print(comment.getText()+'\n')
        onePageComments.append(comment.getText()+'\n')

    return onePageComments


if __name__ == '__main__':
    f = open('avenger.txt', 'w', encoding='utf-8') 
    for page in range(10):  # 豆瓣爬取多页评论需要验证。
        url = 'https://movie.douban.com/subject/26752088/comments?start=' + str(20*page) + '&limit=20&sort=new_score&status=P'
        print('第%s页的评论:' % (page+1))
        print(url + '\n')

        for i in getComment(url):
            f.write(i)
            print(i)
        print('\n')

from wordcloud import WordCloud

import PIL.Image as image

import numpy as np

import jieba

 

# 分词

def trans_CN(text):

	# 接收分词的字符串

    word_list = jieba.cut(text)

    # 分词后在单独个体之间加上空格

    result = " ".join(word_list)

    return result

 
with open('C:/Users/杜敬祎/Desktop/avenger.txt','r',encoding='UTF-8') as f:  # 打开新的文本
    text = f.read()  # 读取文本数据

    # 将读取的中文文档进行分词

    text = trans_CN(text)

    mask = np.array(image.open("C:/Users/杜敬祎/Desktop/love.png"))
    Stopwords = [u'就是', u'电影', u'你们', u'这么', u'不过', u'但是',
                 u'除了', u'时候', u'已经', u'可以', u'只是', u'还是', u'只有', u'不要', u'觉得', u'，',u'。',
                 u'我们',u'一个',u'那么',u'认为',u'最后',u'这个',u'这样']

    wordcloud = WordCloud(

    	# 添加遮罩层

        mask=mask,

        # 生成中文字的字体,必须要加,不然看不到中文

        font_path = "C:/Windows/Fonts/STXINGKA.TTF",
        stopwords=Stopwords

    ).generate(text)

    image_produce = wordcloud.to_image()

    image_produce.show()
wordcloud.to_file('test.jpg')
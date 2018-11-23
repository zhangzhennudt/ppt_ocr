# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 07:07:43 2018

@author:张震
Email：zhangzhennudt@126.com
"""

from aip import AipOcr
import json
import os


# 定义常量
APP_ID = '9851066'
API_KEY = 'LUGBatgyRGoerR9FZbV4SQYk'
SECRET_KEY = 'fB2MNz1c2UHLTximFlC4laXPg7CVfyjV'

# 初始化AipFace对象
aipOcr = AipOcr(APP_ID, API_KEY, SECRET_KEY)

# 读取图片
def get_all_filepath(path):
    filepaths=[]
    for i in range(1,21):
        filepath=path+"/"+str(i)+".png"
        filepaths.append(filepath)
    return filepaths

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

def get_word_from_image(path,txtname):
    f = open(txtname,'a')
    filepaths=get_all_filepath(path)
    count=0
    # 定义参数变量
    options = {
            'detect_direction': 'true',
            'language_type': 'CHN_ENG',
            }
    for filepath in filepaths:
        # 调用通用文字识别接口
        result = aipOcr.basicGeneral(get_file_content(filepath), options)
        result_num=result['words_result_num']# 获得识别文字行数
        result_words=result['words_result']# 获得识别文字行数
        count=count+1
        print("开始识别第%d页"%count+filepath)
        f.writelines("-"*10+"第%d页"%count+"-"*10+'\n')
        for i in range(1,result_num+1):
            f.writelines(result_words[i-1]['words']+'\n')
    print("识别完毕,共识别%d页！"%count)
    f.close()



path="pptimage"
txtname = "result.txt"
get_word_from_image(path,txtname)
































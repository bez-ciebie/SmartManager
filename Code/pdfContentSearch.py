# -*-coding  :  UTF_8 _*_
# 创建时间： 2022/8/24 14:38   # 开发者：Wei Zihao

# *********************************************************
# import sys
import os
import re
import time
from concurrent.futures import  ThreadPoolExecutor, Future
import multiprocessing
from multiprocessing import Pool
# import pip

# import private
import func_timeout

from FileSort import CreateFolder
from pdf2words import pdf2words
# **********************************************************
# 3. 根据文件内容进行搜索。re.findall可以对提取出来的文本内容进行关键字搜索。（pdf信息检索）
#       A.pdf2word获得提取的文本内容
#       B.执行搜索函数（关键字，文本）
#       C.如果包含关键字，输出文件名
#       D.实现对文件夹的遍历搜索
# 线程池写入时，在回调函数写入出现数据不安全，修改为多进程后问题解决。

# 将得到的文件写入txt中
def done(future):
#    if str(future.result()[0]) != str(0):
    print(future)
    if str(future[0]) != str(0):
        with open(Path + "//record_sm.txt", 'a') as f:
            f.writelines(str(future))
            f.write("\n")
        print("sm结果文件已保存到： " + Path + "//record_sm.txt")

# Mode 0:exactly 1:ignore case sensitivity               (origin/lower/upper/title)
# 可以判断输入路径是文件还是文件夹，对pdf进行搜索。如何是其他类型文件，会出错。
def pdfFolderContentSearch(keyword, path, mode):
    #判断是文件还是文件夹,查找时采用进程池优化，防止线程池的数据不安全
    if os.path.isfile(path):
        result_list = pdfContentSearch(keyword, path, mode)
        print("搜索完成："+str(result_list[0])+"个",str(result_list[1]))
    elif os.path.isdir(path):
        multiprocessing.freeze_support()  # 在Windows下编译需要加这行
        list = []
        # 创建进程池
        pool = Pool(4)
        print("开始搜索")
        #对文件夹目录下的文件进行多线程加速搜索
        for home, dirs, files in os.walk(path):
            for filename in files:
                # 向线程池提交一个任务，线程池如果有空余线程，则分配一个线程去执行，执行完毕后将线程交还给线程池，若没有空余线程，则等待。
                r = pool.apply_async(pdfContentSearch, (keyword, os.path.join(home, filename), mode), callback=list.append)
        pool.close()
        pool.join()
        # 等齐了统一保存
        print("搜索完成")
        return list
# Don't search with "()"（pdf信息检索）bug：需要判断文件类型是否为pdf
# Mode 0:exactly 1:ignore case sensitivity               (origin/lower/upper/title)
def pdfContentSearch(keyword, pdf_path, mode):
    #无法查询
    print("正在搜索：" + pdf_path)
    #try:
    # A.pdf2word获得提取的文本内容
    article, count = pdf2words(pdf_path)
    #对获得的内容进行搜索
    if(mode == 0):
        count_keyword = len(re.findall(keyword, article))
        if(count_keyword>0):
            #查询存在
            return [count_keyword, os.path.basename(pdf_path)]
        else:
            #查询不存在
            return [0,os.path.basename(pdf_path)]
    elif(mode == 1):
        count_keyword = len(re.findall(keyword, article))
        count_keyword += len(re.findall(keyword.lower(), article))
        count_keyword += len(re.findall(keyword.upper(), article))
        count_keyword += len(re.findall(keyword.title(), article))
        if(count_keyword>0):
            return [count_keyword, os.path.basename(pdf_path)]
        else:
            return [0,os.path.basename(pdf_path)]
    #except func_timeout.exceptions.FunctionTimedOut:
    #    return [-1,os.path.basename(pdf_path)]
    #except :
    #    return [0, os.path.basename(pdf_path) ]

if __name__ == '__main__':
    # 设置搜索路径
    Path = "D:\paper\demo"

    # keyword, path, mode 0:exactly 1:ignore case sensitivity
    list = pdfFolderContentSearch("bert", Path, 0)
    #x[1]按照文件名称正序排列   x[0]按照关键词数量正序排列
    list = sorted(list, key=lambda x:x[1])
    for one in list:
        if str(one[0]) != str(0):
            with open(Path + "//record_sm.txt", 'a') as f:
                f.writelines(str(one))
                f.write("\n")
            print("sm结果文件已保存到： " + Path + "//record_sm.txt")





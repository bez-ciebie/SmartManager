# -*-coding  :  UTF_8 _*_
# 创建时间： 2022/8/22 16:29   # 开发者：Wei Zihao

# *********************************************************
# import sys

# import pip
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter, PDFPageAggregator
from pdfminer.layout import LAParams
from pdfminer.pdfdevice import PDFDevice
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
import re

# import private
# **********************************************************

# 获取文档对象
def pdf2words(pdf):
    fp=open(pdf,"rb")

    #创建一个与文档关联的解释器
    parser=PDFParser(fp)

    #PDf文档的对象
    doc=PDFDocument(parser)

    #链接解释器和文档对象
    parser.set_document(doc)

    #创建PDF资源管理器
    resource=PDFResourceManager()

    #参数分析器
    laparam=LAParams()

    #创建一个聚合器
    device=PDFPageAggregator(resource,laparams=laparam)

    #创建PDF页面解释器
    interpreter=PDFPageInterpreter(resource,device)

    # 计数器
    passage = ''

    #使用文档对象得到页面的集合
    for page in PDFPage.create_pages(doc):
        #使用页面解释器来读取
        interpreter.process_page(page)

        #使用聚合器来获得内容
        layout=device.get_result()

        # 将文章内容存储到passage变量
        for out in layout:
            if hasattr(out, 'get_text'):  # 需要注意的是在PDF文档中不只有 text 还可能有图片等等，为了确保不出错先判断对象是否具有 get_text()方法完整的代码
                #re函数可以分割多个字符,注意空格的个数
                passage += out.get_text()

    # 使用正则表达式整理文章格式
    passage = re.sub(r'[^A-Za-z ]+', ' ', passage)
    passage = re.sub(r'/t+', ' ', passage)

    # 返回文章和总单词数
    return passage, len(passage.split(" "))



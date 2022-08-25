# -*-coding  :  UTF_8 _*_
# 创建时间： 2022/8/22 15:54   # 开发者：Wei Zihao

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# *****************************************************************************************
#import sys
import sys
#import pip
from PyQt5.QtWidgets import QApplication, QMainWindow

#import private
from FileSort import FileSort, CreateFolder
from QTframe import helloworld
from pdf2words import pdf2words
from pdfContentSearch import pdfFolderContentSearch
# ******************************************************************************************


if __name__ == '__main__':
    folder_path = "D:\\paper\\demo\\0074.pdf"
    #FileSort(folder_path)
    #list = pdfFolderContentSearch("bert", folder_path+"//WORD", 0)
    list = pdfFolderContentSearch("bert", folder_path, 0)









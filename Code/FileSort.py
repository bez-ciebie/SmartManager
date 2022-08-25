# -*-coding  :  UTF_8 _*_
# 创建时间： 2022/8/23 17:25   # 开发者：Wei Zihao

# *********************************************************
# import sys
import os

# import pip
from glob import glob
import shutil

# import private
# **********************************************************
# 2. 对文件中的后缀进行分类归档  word("txt", "pdf", "xlsx", "pptx", "md", "docx")       img("jpg", "jpeg", "png", "bmp", "gif")
#       A.所有文件分类。遍历文件夹下文件名，查找后缀进行分类，将对应文件放到对应文件夹下。
#       B.标记生成的文件夹。文件夹中生成一个目录文件，记录生成文件夹路径参数与文件信息。（所有生成的文件夹可以识别文件是否属于文件夹，并且有标记到独自的出入表中）
#       C.依据出入表指针，在所有管理过的文件中实现快速智能查找。
#       D.优化时使用图结构搜索算法。

documentExtensions = [ "txt", "pdf", "xlsx", "pptx", "md", "docx"]
imageExtensions = [ "jpg", "jpeg", "png", "bmp", "gif" ]

listOfFiles    = []
listOfImages    = []

# 若创建成功文件夹，就写入列表所有文件；若创建失败，不写入文件。
def CreateFolder(folder_name):
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
        print(folder_name+'文件夹创建成功')

def FileSort(folder_path):
    ### Documents 遍历查找放入列表
    for extension in documentExtensions:
        path = folder_path + '//*.' + extension
        listOfFiles.extend( glob(path))
    # 若发现存在word类文件，则写入
    if(len(listOfFiles)>0):
        folder_path_word = folder_path+'//WORD'
        CreateFolder(folder_path_word)
        # 遍历文件列表，向文件夹拷贝文件
        for file in listOfFiles:
            if not os.path.exists(folder_path_word+'//'+file):
                print(file + "已经移动到WORD")
                shutil.move(file, folder_path_word)
                print(file + "已经移动到WORD")  # Or do other stuff
    print("WORD停止传输")

    ### Images 遍历查找放入列表
    for extension in imageExtensions:
        path = folder_path + '//*.' + extension
        listOfImages.extend( glob(path))
    # 若发现存在image类文件，则写入
    if(len(listOfImages)>0):
        folder_path_image = folder_path + '//IMAGE'
        CreateFolder(folder_path_image)
        # 遍历文件列表，向文件夹拷贝文件
        for file in listOfImages:
            if not os.path.exists(folder_path_image+'//'+file):
                shutil.move(file, folder_path_image)
                print(file + "已经移动到IMAGE")  # Or do other stuff
    print("IMAGE停止传输")

if __name__ == '__main__':
    # 定义杂乱文件夹
    folder_path = input("path:")
    # 对文件夹进行分类(对于双下滑线需要进行替换处理)
    FileSort(folder_path)

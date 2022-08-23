# SmartManager
AI manager in your desktop

# 1. 在窗口对pdf文件统计字数，估计阅读时间。 
##       A.完成pdf文件的读写统计字数，并输出字数。 （会生成页眉页脚的文字） 
###           a.获取的字符片段拼接成  文章  ，分词统计字数                                                                                           Done！ 
###           b.获取的字符片段统计 词频 ，计算总数。         words_count = collections.Counter(sentence.translate(punctuation).lower().split()) 
###           c.直接对字符片段计数 
###       B.预计阅读时间   150WPM-300WPM 

# 2. 对文件中的后缀进行分类归档  word(txt pdf docx xlsx pptx md)       img(jpg png jpeg) 
##       A.所有文件分类。遍历文件夹下文件名，查找后缀进行分类，将对应文件放到对应文件夹下。                           done!
##       B.标记生成的文件夹。文件夹中生成一个目录文件，记录生成文件夹路径参数与文件信息。（所有生成的文件夹可以识别文件是否属于文件夹，并且有标记到独自的出入表中）
##       C.依据出入表指针，在所有管理过的文件中实现快速智能查找。
##       D.优化时使用图结构搜索算法。

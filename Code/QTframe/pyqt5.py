# -*-coding  :  UTF_8 _*_
# 创建时间： 2022/8/22 21:20   # 开发者：Wei Zihao

# *********************************************************
# import sys
import sys
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import helloworld

# import private
# **********************************************************


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = helloworld.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

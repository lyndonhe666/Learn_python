from PySide2.QtWidgets import QApplication, QMessageBox
from PySide2.QtUiTools import QUiLoader
from PySide2.QTWidgets import QApplication, QMainWindow, QPushButton, QPlainTextEdit
import pandas as pd

# 要实现的功能
# 1. 读取csv文件，输出班级人数和抽样人数（默认三分之一的班级人数，向上取整）（文本框）
# 2. 按照指定的抽样人数进行抽样（按钮）
# 3. 保存当前抽样的结果到csv(文件名中含时间戳)（按钮）
# 4. 显示全班名单（按钮）
# 5. 推出（按钮）
class Sample():
    def __init__(self):
        # 导入ui文件
        self.ui = QUiLoader().load('qt_exercise1.ui')
        self.data = pd.read_csv('/Users/lyndon/Documents/白月黑羽python/resource/学生名单.csv',encoding='gbk')
        # 显示班级人数
        self.ui.population_number.setPlainText(len(self.data))
        # 设置默认抽样人数
        self.ui.sample_number.setPlainText(int(len(self.data)/3+0.5))
        
    def get_sample(self):
        # 抽样
        data = self.data
        # student id
        sid = (data['序号']).tolist()
        sample_number = int(self.ui.sample_number.toPlainText)
        sample_sids = random.sample(sid, sample_number)
        sample_results = data[data['序号'].isin(sample_sids)]
        

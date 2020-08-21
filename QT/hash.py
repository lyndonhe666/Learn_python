import hashlib
import os
from PySide2.QtWidgets import QApplication, QTextBrowser, QFileDialog
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import Signal, QObject
from threading import Thread
from PySide2 import QtCore
from pathlib import Path

class MySignal(QObject):
    info_print = Signal(QTextBrowser, str)

class FileCheck():
    def __init__(self):
        # self.working_dir = QUiLoader().setWorkingDirectory(ui_path)
        self.ms = MySignal()
        self.ui = QUiLoader().load('QT/hash_compare.ui')
        self.ui.chooseSrcFile.clicked.connect(self.choose_src_file)
        self.ui.makeCheckFile.clicked.connect(self.make_check_file)
        self.ms.info_print.connect(self.print_to_displaybox)
        self.ui.chooseTarFile.clicked.connect(self.choose_tar_file)
        self.ui.chooseCheckFile.clicked.connect(self.choose_check_file)
        self.ui.compareFile.clicked.connect(self.compare_file)

    def print_to_displaybox(self,displaybox, text):
        displaybox.appendPlainText(text)

    def choose_src_file(self):
        selected_dir = QFileDialog.getExistingDirectory(self.ui, "选择需要对比的源文件夹")
        self.ui.displayBox_chosenFile.setPlainText(selected_dir)
    
    def choose_tar_file(self):
        selected_dir = QFileDialog.getExistingDirectory(self.ui, '选择需要对比的目标文件夹')
        self.ui.displayBox_chosenTarFile.setPlainText(selected_dir)
    
    def choose_check_file(self):
        selected_dir, _ = QFileDialog.getOpenFileName(self.ui, '选择校验文件')
        self.ms.info_print.emit(self.ui.displayBox_detail_result, 'Check File chosen:{}'.format(selected_dir))
        with open(selected_dir, 'r') as f:
            self.checked_mdsum =f.read()
    
    def make_check_file(self):
        def thread_make_check_file():
            selected_dir = self.ui.displayBox_chosenFile.toPlainText()
            m=hashlib.md5()
            for dir_path, dir_names, file_names in os.walk(selected_dir):
                for file_name in file_names:
                    fpath = os.path.join(dir_path,file_name)
                    with open(fpath,'rb') as f:
                        contentBytes = f.read()
                        m.update(contentBytes)
                    self.ms.info_print.emit(self.ui.displayBox_detail, 'File: {}'.format(file_name))
            check_file_path = str(Path(selected_dir).parent)+'/'+'check_file.txt'
            with open(check_file_path,'w') as f:
                f.write(m.hexdigest())
            self.ms.info_print.emit(self.ui.displayBox_detail, '校验文件制作完成,保存在:{}'.format(check_file_path))
        thread = Thread(target=thread_make_check_file)
        thread.start()
    
    def compare_file(self):
        self.ui.displayBox_detail_result.clear()
        def thread_compare_file():
            selected_dir = self.ui.displayBox_chosenTarFile.toPlainText()
            m=hashlib.md5()
            for dir_path, dir_names, file_names in os.walk(selected_dir):
                for file_name in file_names:
                    fpath = os.path.join(dir_path, file_name)
                    with open(fpath, 'rb') as f:
                        contentBytes = f.read()
                        m.update(contentBytes)
                    self.ms.info_print.emit(self.ui.displayBox_detail_result,'File: {}'.format(file_name))
            result = m.hexdigest()
            if self.checked_mdsum == result:
                self.ms.info_print.emit(self.ui.displayBox_detail_result, "{}目录下所有文件与源相同".format(selected_dir))
            else:
                self.ms.info_print.emit(self.ui.displayBox_detail_result, "{}目录下有文件已被修改过".format(selected_dir))
        thread = Thread(target=thread_compare_file)
        thread.start()

QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)
app = QApplication([])
fc = FileCheck()
fc.ui.show()
app.exec_()
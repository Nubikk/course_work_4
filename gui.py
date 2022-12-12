
from PyQt6 import QtCore, QtGui, uic, QtWidgets
import os


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        uic.loadUi('course.ui', self)



class Logic(Window):
    def __init__(self):
        super(Logic, self).__init__()
        self.path = r"C:\Users\Flaki\PycharmProjects\pythonProject" #  путь до файла из которого читаем для GUI
        self.info_about_all_pc = dict()

    def ReadFilesNames(self):
        files = []
        for file in os.listdir(self.path):
            if os.path.isfile(os.path.join(self.path, file)):
                files.append(file)
        return files

    def CompilateFiles(self):
        files = self.ReadFilesNames()
        files_to_read = []
        for file in files:
            if '.txt' in file:
                files_to_read.append(self.path+file)
        return files_to_read

    def ReadFiles(self):
        #files = self.CompilateFiles()
        data = ''
        #for file in files:
        with open("Nubikk.txt", 'r') as f:
            #f = open(r'C:\Users\Flaki\PycharmProjects\pythonProject\text.txt', 'r')
            cnt = 0
            for line in f:
                data = line
                if cnt == 1:
                    break
                cnt += 1
                #data = line
                #break
            all_data =''
            all_data += 'INFO ABOUT SYSTEM\n'
            all_data += f.read()
            name = data[10:len(data)-1:]
            self.info_about_all_pc[name] = all_data
        f.close()

    def FillComboBox(self):
        self.ReadFiles()
        self.info_about_all_pc['FLAKI'] = 'TEST TEST TEST'
        self.comboBox.addItems([str(i) for i in self.info_about_all_pc.keys()])

    def FillInfo(self):
        self.ReadFiles()
        name = self.comboBox.currentText()
        self.plainTextEdit.clear()
        self.plainTextEdit.appendPlainText(self.info_about_all_pc[name])

    def push(self):
        self.pushButton.clicked.connect(self.FillInfo)

    def show_gui(self):
        self.FillComboBox()
        self.FillInfo()
        self.push()
        self.show()





app = QtWidgets.QApplication([])
win = Window()
l = Logic()
l.show_gui()
app.exec()




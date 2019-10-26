import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import *
import pyqrcode
import requests
from PIL import Image

state = False
response = None
qr_show = None

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'promptplay'
        # self.left = 10
        # self.top = 10
        # self.width = 640
        # self.height = 480
        # self.initUI()

        self.timer = QTimer()
        self.timer.setInterval(2)
        self.timer.timeout.connect(self.maim_task)
        self.timer.start()

    def initUI(self):
        self.setWindowTitle(self.title)
        # self.setGeometry(self.left, self.top, self.width, self.height)
        # Create widget
        label = QLabel(self)
        pixmap = QPixmap('url.png')
        label.setPixmap(pixmap)
        self.resize(pixmap.width(),pixmap.height())
        self.show()

    def maim_task(self):
        global state
        global response
        global qr_show

        part_file = "C:/Users/Natchaipon/Documents/promptplay/url.png"

        if state == False:
            gen_id = requests.get('https://scb.azurewebsites.net/api/Qr')
            response = gen_id.json()
            # print(response)
            url = pyqrcode.create(response['data']['qrRawData'])
            url.png(part_file , scale=2)
            self.setWindowTitle(self.title)
            label = QLabel(self)
            pixmap = QPixmap(part_file)
            label.setPixmap(pixmap)
            self.resize(pixmap.width(),pixmap.height())
            self.show()
            # qr_show = Image.open(part_file)
            # qr_show.show()
            # time.sleep(5)
            # print(qr_show.bits, qr_show.size, qr_show.format)
            # qr_show.close()
            state = True

        if state == True:
            check_money = requests.get('https://scb.azurewebsites.net/api/verify/' + str(response['verifyId']))
            response_check_money = check_money
            if response_check_money.text == 'true':
                print("ชำระเงินสำเร็จแล้ว")
                self.close()
                # qr_show.close()
                state = False



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
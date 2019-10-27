import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets
from ui_main import Ui_MainWindow
import pyqrcode
import requests
from PIL import Image
from line_notify import line_notify
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(13,GPIO.OUT)

GPIO.output(13,GPIO.HIGH)

state = False
response = None
qr_show = None

class MyApp(QMainWindow):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.timer = QTimer()
        self.timer.setInterval(2)
        self.timer.timeout.connect(self.maim_task)
        self.timer.start()

    def maim_task(self):
        global state
        global response
        global qr_show

        part_file = "url.png"

        try:
            if state == False:
                gen_id = requests.get('https://scb.azurewebsites.net/api/Qr')
                response = gen_id.json()
                print(response)
                url = pyqrcode.create(response['data']['qrRawData'])
                url.png(part_file , scale=5)
                self.label = QtWidgets.QLabel()
                self.ui.label.setText("")
                self.ui.label.setPixmap(QtGui.QPixmap(part_file))
                self.ui.label.setObjectName("label")

                # self.ui.label.setPixmap(QtGui.QPixmap("C:/Users/Natchaipon/Documents/promptplay/url.png"))
                    # self.setWindowTitle(self.title)
                    # label = QLabel(self)
                    # pixmap = QPixmap(part_file)
                    # label.setPixmap(pixmap)
                    # self.resize(pixmap.width(),pixmap.height())
                    # self.show()


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
                    line_notify()
                    GPIO.output(13 , GPIO.LOW)
                    time.sleep(5)
                    GPIO.output(13 , GPIO.HIGH)
                    # self.close()
                        # qr_show.close()
                    state = False
        except:
            pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myapp = MyApp()
    myapp.show()
    sys.exit(app.exec_())

# importing modules
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import * 
import sys
import winsound

def timeoutPlay():
    print('timer out!')
    winsound.PlaySound("*", winsound.SND_ALIAS|winsound.SND_ASYNC)
    print('timer out!!')

class Canvas(QWidget):
    def __init__(self):
        super().__init__()

        button1 = QPushButton(self)
        button1.setText("分钟")
        button1.setFixedSize(100,50)
        button1.move(200,350)
        button1.pressed.connect(self.setMin)

        self.goStopButton = QPushButton(self)
        # self.goStopButton.setText("走/停")
        self.setButtonIcon(self.goStopButton, 'play')
        self.goStopButton.move(350,350)
        self.goStopButton.setFixedSize(100,50)
        self.goStopButton.pressed.connect(self.goStop)


        button3 = QPushButton(self)
        button3.setText("秒钟")
        button3.setFixedSize(100,50)
        button3.move(500,350)
        button3.pressed.connect(self.setSec)

        button4 = QPushButton(self)
        button4.setText("清零")
        button4.move(350,275)
        button4.setFixedSize(100,50)
        button4.pressed.connect(self.clear)

        self.minDisplay = QLCDNumber(self)
        self.minDisplay.setDigitCount(2)
        self.minDisplay.setFixedSize(100, 100)
        self.minDisplay.move(300, 150)

        self.secDisplay = QLCDNumber(self)
        self.secDisplay.setDigitCount(2)
        self.secDisplay.setFixedSize(100, 100)
        self.secDisplay.move(400, 150)

        self.recPosition = [10,10]
        self.recSize = [100,100]

        self.minSet = 0
        self.secSet = 0

        self.minRemain = 0
        self.secRemain = 0

        self._timer = QTimer()
        self._timer.timeout.connect(self.timerTick)

        self.updateLcd()
        

    def setButtonIcon(self, button, status):
        style = button.style() # Get the QStyle object from the widget.
        if status == 'play':
            iconPlay = style.standardIcon(QStyle.SP_MediaPlay)
            button.setIcon(iconPlay)
        elif status == 'pause':
            iconPause = style.standardIcon(QStyle.SP_MediaPause)
            button.setIcon(iconPause)
            

    def updateLcd(self):
        self.minDisplay.display(self.minRemain)
        self.secDisplay.display(self.secRemain)
    
    def settingShowLcd(self):
        self.minDisplay.display(self.minSet)
        self.secDisplay.display(self.secSet)

    def timerTick(self):
        self.secRemain -= 1
        print('1s tick')

        if self.secRemain == -1 and self.minRemain != 0:
            self.secRemain = 59
            self.minRemain -= 1
            self.updateLcd()
        else:
            self.updateLcd()

        if self.secRemain == 0 and self.minRemain == 0:
            self.setButtonIcon(self.goStopButton, 'play')
            self.settingShowLcd()
            self._timer.stop()
            timeoutPlay()

    def clear(self):
        if not self._timer.isActive():
            self.secSet = 0
            self.minSet = 0
            self.secRemain = 0
            self.minRemain = 0
            self.settingShowLcd()

    def paintEvent(self, event):
        painter = QPainter(self)
        pen = QPen(Qt.black, 4)
        painter.setPen(pen)

        painter.drawRect(150, 100, 500, 350)
        painter.end()

    def setMin(self):
        if not self._timer.isActive():
            self.minSet += 1
            if self.minSet >= 100:
                self.minSet = 0
            self.settingShowLcd()

    def goStop(self):
        if self.secSet == 0 and self.minSet == 0:
            timeoutPlay()
            return
        elif self._timer.isActive():
            self.setButtonIcon(self.goStopButton, 'play')
            self._timer.stop()
        elif not self._timer.isActive():
            self.setButtonIcon(self.goStopButton, 'pause')
            if self.secRemain == 0 and self.minRemain == 0:
                self.secRemain = self.secSet
                self.minRemain = self.minSet
            self.updateLcd()
            self._timer.start(1000)

    def setSec(self):
        if not self._timer.isActive():
            self.secSet += 1
            if self.secSet >= 60:
                self.secSet = 0
            self.settingShowLcd()


# creating class for window
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.centralWidget = Canvas()
        self.setCentralWidget(self.centralWidget)
        self.setFixedSize(800, 600)


# main method
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    
    # looping for window
    sys.exit(app.exec())

# Notes
# 目前这版基本能用，不过实现的方式还是比较乱，没啥章法
# 优化方向是，先定义计时器的状态：setting, ticking, warning
# 然后根据计时器状态来处理对应中断的处理方式
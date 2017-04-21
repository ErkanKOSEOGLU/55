import sys
from PyQt4 import QtGui, QtCore
import numpy as np
import pyqtgraph as pg


class sinus_wave(QtGui.QWidget):

    def __init__(self):
        super(sinus_wave, self).__init__()

        self.initUI()


    def initPlot(self, plots):
        a = 10
        ptr1 = 30

        data1 = a*np.sin(np.linspace(0,30,121))
        plots.plot(data1)

        timer = pg.QtCore.QTimer()
        timer.timeout.connect(lambda: self.update(self,p1 = plots,data1= data1, ptr1 = ptr1))
        timer.start(50)

    def initUI(self):


        IncreaseButton = QtGui.QPushButton("Increase Amplitude")
        DecreaseButton = QtGui.QPushButton("Decrease Amplitude")
        p1 = pg.PlotWidget()

        hbox = QtGui.QVBoxLayout()
        hbox.addWidget(p1)
        hbox.addWidget(IncreaseButton)
        hbox.addWidget(DecreaseButton)

        self.initPlot(p1)
        self.setLayout(hbox)

        self.setGeometry(10, 10, 1000, 600)
        self.setWindowTitle('Sinuswave')
        self.show()


    def update(self, p1, data1, ptr1):

        data1[:-1] = data1[1:]
        data1[-1] = np.sin(ptr1/4)
        p1.plot(data1)
        ptr1 += 1
        p1.show()

    def IncreaseButtonClick(self):
        print ("Amplitude increased")

    def DecreaseButtonClick(self):
        print ("Amplitude decreased")


def main():

    app = QtGui.QApplication(sys.argv)
    app.setApplicationName('Sinuswave')
    ex = sinus_wave()

    sys.exit(app.exec_())

if __name__ == '__main__':

    main()


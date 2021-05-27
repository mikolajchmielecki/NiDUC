
from PyQt5.QtCore import QObject, QThread, pyqtSignal
from Etap3.ChannelSingle import *
from Etap3.ChannelGroup import *
from Etap3.BCHCoder import *
from Etap3.Threads import runLongTask
from Etap3.TripleCoder import *
from Etap3.Generator import *
from Etap3.Simulation import *
from Etap3.Tests import *
from Etap3.Plots import *
from Etap3.Window import *
from Etap3.Logging import *
from os import environ

"""
Wyłącza ostrzeżenia PyQT
"""
def suppress_qt_warnings():
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"

coders = []
coders.append(TripleCoder(20, True))
coders.append(TripleCoder(20, False))
coders.append(BCHCoder(3, 1))
coders.append(BCHCoder(4, 1))
coders.append(BCHCoder(4, 2))
coders.append(BCHCoder(4, 3))
coders.append(BCHCoder(5, 1))
coders.append(BCHCoder(5, 2))
coders.append(BCHCoder(5, 3))
coders.append(BCHCoder(5, 5))
coders.append(BCHCoder(5, 7))
coders.append(BCHCoder(6, 1))
coders.append(BCHCoder(6, 2))
coders.append(BCHCoder(6, 3))
coders.append(BCHCoder(6, 4))
coders.append(BCHCoder(6, 5))
coders.append(BCHCoder(6, 6))
coders.append(BCHCoder(6, 7))
coders.append(BCHCoder(6, 10))
coders.append(BCHCoder(6, 11))
coders.append(BCHCoder(6, 13))
coders.append(BCHCoder(6, 15))


"""
Uruchamia testy w zależności od wprowadzonych parametrów
"""
def run(MainWindow, ui, logger):
    selected_coders = []

    # sprawdzenie wybranych checkboxów
    i = 0
    for checkBox in ui.checkBoxList:
        if checkBox.isChecked():
            selected_coders.append(coders[i])
        i += 1

    if not selected_coders:
        return

    generator = Generator(ui.spinBox.value())
    msg = generator.generate_signal()

    # wybór kanału
    channel = None
    if ui.single.isChecked():
        channel = ChannelSingle(ui.doubleSpinBox.value())
    if ui.group.isChecked():
        channel = ChannelGroup(ui.doubleSpinBox.value())

    tests = Tests(selected_coders, channel)
    runLongTask(MainWindow, logger, msg, channel, tests)


"""
Wyświetla okienko
"""
if __name__ == "__main__":
    suppress_qt_warnings()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    MainWindow.isBusy = False
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow, coders)
    logger = Logger()
    def button_clicked():
        logger.show()
        run(MainWindow, ui, logger)

    ui.pushButton.clicked.connect(button_clicked)
    MainWindow.show()

    sys.exit(app.exec_())
















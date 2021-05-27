"""
Rozwiązuje problem wiszącego okna podczas przeprowadzania symulacji
https://realpython.com/python-pyqt-qthread/
"""
from PyQt5.QtCore import QObject, QThread, pyqtSignal
# Snip...

# Step 1: Create a worker class
from Etap3.Plots import plot_BER_E


class Worker(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(int)

    def __init__(self, tests, msg):
        super().__init__()
        self.tests = tests
        self.msg = msg
        self.results = None

    def run(self):
        """Long-running task."""
        self.results = self.tests.run(self.msg)
        self.finished.emit()


"""
Długie zadania
Wyzwala symulacje i przechwtywuje wynik
"""
def runLongTask(MainWindow, logger, msg, channel, tests):

    if MainWindow.isBusy:
        return
    # Step 2: Create a QThread object
    MainWindow.thread = QThread()
    # Step 3: Create a worker object
    MainWindow.worker = Worker(tests, msg)
    # Step 4: Move worker to the thread
    MainWindow.worker.moveToThread(MainWindow.thread)
    # Step 5: Connect signals and slots
    MainWindow.thread.started.connect(MainWindow.worker.run)
    MainWindow.worker.finished.connect(MainWindow.thread.quit)
    MainWindow.worker.finished.connect(MainWindow.worker.deleteLater)
    MainWindow.thread.finished.connect(MainWindow.thread.deleteLater)
    # Step 6: Start the thread
    MainWindow.thread.start()
    MainWindow.isBusy = True

    MainWindow.thread.finished.connect(
        lambda: worker_finish(MainWindow, logger, msg, channel, tests)
    )


def worker_finish(MainWindow, logger, msg, channel, tests):
    plot_BER_E(MainWindow.worker.results, channel, msg)
    logger.hide()
    MainWindow.isBusy = False

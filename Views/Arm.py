import sys

from PyQt5.QtWidgets import QApplication

from Views.Armory_ui import Armory

app = QApplication(sys.argv)

MainWindow = Armory()
MainWindow.show()
sys.exit(app.exec_())

import sys
from PyQt5 import QtWidgets
from MarioParty import MarioParty

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MarioPartyWindow = QtWidgets.QMainWindow()
    marioPartyUi = MarioParty()
    marioPartyUi.init(MarioPartyWindow)
    MarioPartyWindow.show()
    sys.exit(app.exec_())

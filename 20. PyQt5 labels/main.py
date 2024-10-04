import sys
from  PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("First GUI")
        self.setGeometry(100,200,700,700)

        label=QLabel("Home",self)
        label.setFont(QFont("Arial",20,True))
        label.setGeometry(0,0,500,500)
        label.setStyleSheet("color:green;"
                       "background-color:#235054;"
                       "font-style:italic;"
                       "font-weight:bold;")

        # label.setAlignment(Qt.AlignTop)
        # label.setAlignment(Qt.AlignBottom)
        # label.setAlignment(Qt.AlignVCenter)


        # label.setAlignment(Qt.AlignRight)
        # label.setAlignment(Qt.AlignLeft)
        # label.setAlignment(Qt.AlignHCenter)


        # label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)

        #for both horizontal and vertical alignment
        label.setAlignment(Qt.AlignCenter)
    

def main():
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
from PyQt5.QtWidgets import QApplication
from PyQt5.uic import loadUi
import os

#............................................

def mainn():
    filename = windows.le1.text()# Ex: C:\\\Users\\\kakois\\\Documents\\\python progect main\\\Gawla Akhera or use r for row input
    print(filename)
    name = windows.le2.text()# Ex: Gawla Akhera EP

    en=1

    try:
        for i in os.listdir(filename):
            In_file=i
            os.rename( f"{filename}\\\{i}",f"{filename}\\\{name} {en}.mp4")
            en+=1
            print(f"{i}")
    except PermissionError:
        print(f"Permission denied: '{filename}'")
    except FileNotFoundError:
        print(f"File not found: '{filename}'")

#............................................

def annuler():
    windows.le1.setText("")
    windows.le2.setText("")

#.............................................

app=QApplication([])
windows=loadUi("IntGra.ui")
windows.show()
windows.br.clicked.connect(mainn)
windows.bre.clicked.connect(annuler)
windows.bc.clicked.connect(windows.close)
app.exec_()
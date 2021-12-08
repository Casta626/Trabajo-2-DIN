import sys
from PySide6.QtWidgets import QApplication, QListWidget, QListWidgetItem, QMainWindow, QPushButton

from ui_design import Ui_MainWindow
import recursos_rc
import json

class MainWindow(QMainWindow,Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        try:
           self.diccionario = {}
           with open("tareas.json") as fichero:
            
            self.diccionario = json.load(fichero)
            self.contador = 0
            for i in self.diccionario:
              #self.contador = i
              #self.contador = str(i) #?????
              self.t1.addItem(QListWidgetItem(self.diccionario.get(i)))
              
        except Exception:
          self.diccionario = {}


        self.actionNueva_Tarea.triggered.connect(self.nuevaTarea)
        self.b1.clicked.connect(self.nuevaTarea)
        
        self.actionEliminar_Tarea.triggered.connect(self.eliminarTarea)
        self.b2.clicked.connect(self.eliminarTarea)
        

   
        #keys, values, clean, copy, get, pop          Tonny

    def nuevaTarea(self):
        
        textoT2=self.t2.toPlainText()
        #contador = 0
        self.diccionario[self.contador] = textoT2
        self.t1.addItem(QListWidgetItem(self.diccionario.get(self.contador)))  #dentro del get poner el ultimo indice.
        self.contador+=1
        self.t2.clear()
        with open("tareas.json", "w") as fichero:
          json.dump(self.diccionario, fichero)
        

    def eliminarTarea(self):
      self.t1.takeItem(self.t1.indexFromItem(self.t1.currentItem()).row())
      idEliminado= str((self.t1.indexFromItem(self.t1.currentItem()).row()))
      print(idEliminado)
      #self.diccionario.pop(idEliminado)
      #hay que sumar 1
      print((self.t1.indexFromItem(self.t1.currentItem()).row()))
      with open("tareas.json", "w") as fichero:
        json.dump(self.diccionario, fichero)
      self.diccionario = json.load(fichero)
     



        
        

     
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
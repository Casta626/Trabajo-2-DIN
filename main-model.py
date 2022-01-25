import sys
from typing import Union
from PySide6.QtCore import QAbstractListModel, QStringConverter, QStringListModel, Qt
from PySide6.QtWidgets import QApplication, QListWidget, QListWidgetItem, QMainWindow, QPushButton

from ui_designmodel import Ui_MainWindow
import recursos_rc
import json

class TaskModel(QAbstractListModel,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.task = ["cero","uno","dos","tres","cuatro"]
        
          
        

    def actualizarDatosModelo(self):
          # Actualizar la vista del modelo de datos
        # Cuando los datos de un modelo cambian (se añade o se elimina una tarea), hay que actualizar la vista del objeto listView. Se hace de la siguiente forma (siendo self.model el atributo que almacena el modelo):
        self.model.layoutChanged.emit()

###################################################################################################################################################

    def indicesSeleccionados(self):
      
          # Acceder a los elementos seleccionados
        # El método selectedIndexes() devuelve un array de los índices de los elementos que estén seleccionados en el objeto listView:
        indexes = self.listView.selectedIndexes()
        if len(indexes) == 1:
          indexes[0].row()
           # Si solamente hay un elemento seleccionado, el índice de ese elemento será indexes[0].row().
      
    def clearSelection(self):
        # Desmarcar una selección en un listView
        # Después de eliminar un elemento, sería bueno desmarcar cualquier selección en el listView. Se puede hacer con el método clearSelection():
          self.listView.clearSelection()

###################################################################################################################################################

    def data(self,index,role):
      if role == Qt.DisplayRole:
        return self.task[index.row()]
      
        

    def rowCount(self,index):
      index = len(self.task)
      return index
        

    

class MainWindow(QMainWindow,Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Declarar y usar el modelo de datos
        # Declarar el modelo es tan fácil como crear una instancia de la clase creada previamente:
        self.model = TaskModel()
        # Para asignarlo a un objeto listView, se utiliza el método setModel:
        self.listView.setModel(self.model)

        self.contador = 0
        self.contador2 = 0

        self.guardarTarea()
       
        self.actionNueva_Tarea.triggered.connect(self.nuevaTarea)
        self.b1.clicked.connect(self.nuevaTarea)
        self.actionGuardar.triggered.connect(self.guardarTarea)
        self.actionEliminar_Tarea.triggered.connect(self.eliminarTarea)
        self.b2.clicked.connect(self.eliminarTarea)
        self.actionGuardar_Como.triggered.connect(TaskModel.data)
        self.actionNuevo_Archivo.triggered.connect(TaskModel.rowCount)
        
    # metodo eliminar pop    añadir append   ambos layout changed
    def guardarComo(self):
      
      print("F7")

    def nuevaTarea(self):
        textoT2=self.t2.toPlainText()
        self.diccionario[self.contador2] = textoT2
        
        self.contador2+=1
        self.t2.clear()
        self.model.layoutChanged.emit()
       
        
    def guardarTarea(self):
      
      self.contador2=0
      
      self.diccionario2={}
      self.diccionario2.clear()

      for i in self.diccionario:
        self.diccionario2[str(self.contador2)] = self.diccionario.get(i)
        self.contador2+=1

      with open("tareas2.json", "w") as fichero:
        json.dump(self.diccionario2, fichero)
      

    def eliminarTarea(self):
      
      self.guardarTarea()
      self.t1.takeItem(self.t1.indexFromItem(self.t1.currentItem()).row())
      idEliminado= (self.t1.indexFromItem(self.t1.currentItem()).row())
      # idReal=str(idEliminado)
      # if idReal==-1:
        # idReal=0
      # self.diccionario.pop(idReal) 
      self.model.layoutChanged.emit()

      print((self.t1.indexFromItem(self.t1.currentItem()).row()))
      # print(idReal)
      self.guardarTarea()
      self.diccionario = self.diccionario2
      with open("tareas2.json", "w") as fichero:
        json.dump(self.diccionario, fichero)
      
      
      

app = QApplication(sys.argv)
window = MainWindow()
window.setWindowTitle('Mis Tareas')
window.show()
app.exec()
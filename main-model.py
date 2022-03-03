import sys
from typing import Union
from PySide6.QtCore import QAbstractListModel, QStringConverter, QStringListModel, Qt
from PySide6.QtWidgets import QApplication, QListWidget, QListWidgetItem, QMainWindow, QPushButton, QListView

from ui_designmodel import Ui_MainWindow
import recursos_rc
import json

class TaskModel(QAbstractListModel,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.task = []
        # self.task2 = []
        # # self.task = {"0": "cero"}
        # with open("tareas2.json") as fichero:
        #      self.task = json.load(fichero)
        
        # for i in self.task:
        #    self.task2.append(i)

        # self.task = self.task2
        # # self.task2
        # self.task2.append("ocho")
        # self.task2.pop(0)
        # self.diccionario = {}

        # self.task = ["cero","uno","dos","tres","cuatro"]
        
        
          
        

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

        try:
          with open("tareas2.json") as fichero:
            self.model.task = json.load(fichero)
        except Exception:
          self.model.task = []

        # Para asignarlo a un objeto listView, se utiliza el método setModel:
        self.listView.setModel(self.model)
   
        self.actionNueva_Tarea.triggered.connect(self.nuevaTarea)
        self.b1.clicked.connect(self.nuevaTarea)
        # self.actionGuardar.triggered.connect(self.guardarTarea)
        self.actionEliminar_Tarea.triggered.connect(self.eliminarTarea)
        self.b2.clicked.connect(self.eliminarTarea)
        self.actionGuardar_Como.triggered.connect(TaskModel.data)
        self.actionNuevo_Archivo.triggered.connect(TaskModel.rowCount)
        
    # metodo eliminar pop    añadir append   ambos layout changed
    def guardarComo(self):
      
      print("F7")

    def nuevaTarea(self):

        textoT2=self.t2.toPlainText()

        self.model.task.append(textoT2)

        self.model.layoutChanged.emit()

        with open("tareas2.json", "w") as fichero:
          json.dump( self.model.task, fichero) 

    def eliminarTarea(self):

      indice = self.listView.selectedIndexes()

      self.model.task.pop(indice[0].row())

      self.model.layoutChanged.emit()

      with open("tareas2.json", "w") as fichero:
        json.dump(self.model.task, fichero)
      
      
      

app = QApplication(sys.argv)
window = MainWindow()
window.setWindowTitle('Mis Tareas')
window.show()
app.exec()
import sys
from PySide6.QtWidgets import QApplication, QListWidget, QListWidgetItem, QMainWindow, QPushButton

from ui_design import Ui_MainWindow
import recursos_rc
import json
'''
try
  tareas =  '{ "1":"Limpiar", "23":"Sacar la basura", "453":"Fregar"}'
  diccionarioTareas = json.loads(tareas)
  diccionarioTareas["1"] = "Activar robot de limpieza"
  tareas = json.dumps(diccionarioTareas)
  print(tareas)
  with open("tareas.json", "w") as file:
    json.dump(tareas, file)
  with open("tareas.json") as fichero:
              tareas = json.load(fichero)
  tareasLista = '["Limpiar", "Sacar la basura", "Fregar"]'
  tareasJson = json.loads(tareasLista)

  self.listWidget.addItem(QListWidgetItem(self.data.get(task)))
  Siendo:
  listWidget: El nombre del componente QListWidget
  t1
  self.data: Un diccionario con los pares (identificador de la tarea, descripción de la tarea)

  task: El elemento del diccionario self.data que desea mostrarse

  json<---->diccionario--->Lista

  task =  { "1":"Limpiar", "23":"Sacar la basura", "453":"Fregar"}
  self.data = task
  self.t1.addItem(QListWidgetItem(self.data.get("1")))
  with open("tareas.json", "w") as fichero:
  json.dump(self.data, fichero)

  listWidget: El nombre del componente QListWidget
  t1
  self.data: Un diccionario con los pares (identificador de la tarea, descripción de la tarea)

  task: El elemento del diccionario self.data que desea mostrarse
'''
#Logica boton borrar;   self.t1.takeItem(self.t1.indexFromItem("funcion para pillar el elemento seleccionado").row())
#"Limpiar" el diccionario

'''
el texto de t2 sea transmitido a tal indice del diccionario
Llamar a la lista con addItem y añadir un elemento a la lista
Mirar metodos del addItem.
'''

class MainWindow(QMainWindow,Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        try:
           
           with open("tareas.json") as fichero:
            self.diccionario = json.load(fichero)
            #bucle, añadir con el addItem (i)
            
            self.contador = 0
            self.contador2 = 0
            self.cont = str(self.contador2)

            for i in self.diccionario:
              self.t1.addItem(QListWidgetItem(self.diccionario.get(i)))

            self.guardarTarea()
            
              
        except Exception:
          self.diccionario = {}


        self.actionNueva_Tarea.triggered.connect(self.nuevaTarea)
        self.b1.clicked.connect(self.nuevaTarea)
        self.actionGuardar.triggered.connect(self.guardarTarea)
        self.actionEliminar_Tarea.triggered.connect(self.eliminarTarea)
        self.b2.clicked.connect(self.eliminarTarea)
        self.actionGuardar_Como.triggered.connect(self.guardarComo)
        

    def guardarComo(self):
      #Crear el contador para la id del diccionario
      #Crear el string que va a recibir de nuevaTarea
      #Crear el bucle para que cada vez que se añada una nueva tarea se sume el contador y machaque el valor anterior del string
      #Retornarlo todo en un String con la id correspondiente
      #Luego lo podría pasar los strings en un array para buscar el [-1] que siempre será el ultimo

      #https://docs.hektorprofe.net/python/programacion-de-funciones/retorno-de-valores/

      #contador=1
      #for i in contador:

       # contador+1
      print(self.diccionario)
      print(self.diccionario2)

#crear un contador para la id y asociarlo al texto de t2, en el get poner solo la id y ya te muestra el contenido.

        #keys, values, clean, copy, get, pop          Tonny

    def nuevaTarea(self):
        
        textoT2=self.t2.toPlainText()
        #contador = 0
        self.diccionario[self.contador2] = textoT2
        self.t1.addItem(QListWidgetItem(self.diccionario.get(self.contador2)))  #dentro del get poner el ultimo indice.
        self.contador2+=1
        self.t2.clear()
        with open("tareas.json", "w") as fichero:
          json.dump(self.diccionario, fichero)
        



    def guardarTarea(self):
      self.contador2=0
      
      self.diccionario2={}
      self.diccionario2.clear()

      for i in self.diccionario:
        self.diccionario2[str(self.contador2)] = self.diccionario.get(i)
        self.contador2+=1

      with open("tareas.json", "w") as fichero:
        json.dump(self.diccionario2, fichero)


    def eliminarTarea(self):
      self.guardarTarea()
      idEliminado= (self.t1.indexFromItem(self.t1.currentItem()).row())
      self.t1.takeItem(self.t1.indexFromItem(self.t1.currentItem()).row())
      
      idReal=str(idEliminado)
      if idReal==-1:
        idReal=0
      self.diccionario.pop(idReal)
      #hay que sumar 1
      print((self.t1.indexFromItem(self.t1.currentItem()).row()))
      print(idReal)
      self.guardarTarea()
      self.diccionario = self.diccionario2
      with open("tareas.json", "w") as fichero:
        json.dump(self.diccionario, fichero)


        
        

     
app = QApplication(sys.argv)
window = MainWindow()
window.setWindowTitle('Mis Tareas')
window.show()
app.exec()
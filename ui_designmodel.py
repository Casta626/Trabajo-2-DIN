# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QListView, QListWidget, QListWidgetItem,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTextEdit, QToolBar,
    QVBoxLayout, QWidget)
import recursos_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(735, 716)
        palette = QPalette()
        brush = QBrush(QColor(227, 227, 227, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        brush1 = QBrush(QColor(51, 153, 255, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Highlight, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        brush2 = QBrush(QColor(240, 240, 240, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Highlight, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Highlight, brush1)
        MainWindow.setPalette(palette)
        MainWindow.setStyleSheet(u"background-color: rgb(227, 227, 227);")
        self.actionCopiar = QAction(MainWindow)
        self.actionCopiar.setObjectName(u"actionCopiar")
        icon = QIcon()
        icon.addFile(u":/iconos/copy.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionCopiar.setIcon(icon)
        self.actionCortar = QAction(MainWindow)
        self.actionCortar.setObjectName(u"actionCortar")
        icon1 = QIcon()
        icon1.addFile(u":/iconos/cut.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionCortar.setIcon(icon1)
        self.actionPegar = QAction(MainWindow)
        self.actionPegar.setObjectName(u"actionPegar")
        icon2 = QIcon()
        icon2.addFile(u":/iconos/paste.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionPegar.setIcon(icon2)
        self.actionNuevo_Archivo = QAction(MainWindow)
        self.actionNuevo_Archivo.setObjectName(u"actionNuevo_Archivo")
        icon3 = QIcon()
        icon3.addFile(u":/iconos/File.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionNuevo_Archivo.setIcon(icon3)
        self.actionAbrir_Archivo = QAction(MainWindow)
        self.actionAbrir_Archivo.setObjectName(u"actionAbrir_Archivo")
        icon4 = QIcon()
        icon4.addFile(u":/iconos/open file.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionAbrir_Archivo.setIcon(icon4)
        self.actionGuardar = QAction(MainWindow)
        self.actionGuardar.setObjectName(u"actionGuardar")
        icon5 = QIcon()
        icon5.addFile(u":/iconos/save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionGuardar.setIcon(icon5)
        self.actionGuardar_Como = QAction(MainWindow)
        self.actionGuardar_Como.setObjectName(u"actionGuardar_Como")
        self.actionGuardar_Como.setIcon(icon5)
        self.actionNueva_Tarea = QAction(MainWindow)
        self.actionNueva_Tarea.setObjectName(u"actionNueva_Tarea")
        icon6 = QIcon()
        icon6.addFile(u":/iconos/task.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionNueva_Tarea.setIcon(icon6)
        self.actionEliminar_Tarea = QAction(MainWindow)
        self.actionEliminar_Tarea.setObjectName(u"actionEliminar_Tarea")
        icon7 = QIcon()
        icon7.addFile(u":/iconos/cross.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionEliminar_Tarea.setIcon(icon7)
        self.actionDeshacer = QAction(MainWindow)
        self.actionDeshacer.setObjectName(u"actionDeshacer")
        icon8 = QIcon()
        icon8.addFile(u":/iconos/undo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionDeshacer.setIcon(icon8)
        self.actionRehacer = QAction(MainWindow)
        self.actionRehacer.setObjectName(u"actionRehacer")
        icon9 = QIcon()
        icon9.addFile(u":/iconos/redo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionRehacer.setIcon(icon9)
        self.actionLimpiar = QAction(MainWindow)
        self.actionLimpiar.setObjectName(u"actionLimpiar")
        icon10 = QIcon()
        icon10.addFile(u":/iconos/broom.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionLimpiar.setIcon(icon10)
        self.actionMostrar = QAction(MainWindow)
        self.actionMostrar.setObjectName(u"actionMostrar")
        self.actionOcultar = QAction(MainWindow)
        self.actionOcultar.setObjectName(u"actionOcultar")
        self.actionMostrar_2 = QAction(MainWindow)
        self.actionMostrar_2.setObjectName(u"actionMostrar_2")
        self.actionOcultar_2 = QAction(MainWindow)
        self.actionOcultar_2.setObjectName(u"actionOcultar_2")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background/color:#ffff00")
        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(10, 10, 581, 591))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.listView = QListView(self.verticalLayoutWidget_2)
        self.listView.setObjectName(u"listView")
        self.listView.setStyleSheet(u"QListView{\n"
" font: 10pt \"Ink Free\";\n"
" border: 2px solid whitesmoke;\n"
" border-radius: 5px;\n"
" background-color: rgb(255, 251, 192);\n"
"}\n"
"")

        self.verticalLayout_3.addWidget(self.listView)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.t2 = QTextEdit(self.verticalLayoutWidget_2)
        self.t2.setObjectName(u"t2")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.t2.sizePolicy().hasHeightForWidth())
        self.t2.setSizePolicy(sizePolicy)
        self.t2.setStyleSheet(u"QWidget{\n"
" font: 10pt \"Ink Free\";\n"
" border: 2px solid whitesmoke;\n"
" border-radius: 5px;\n"
" background-color: rgb(255, 255, 135);\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.t2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.b3 = QPushButton(self.verticalLayoutWidget_2)
        self.b3.setObjectName(u"b3")
        self.b3.setStyleSheet(u"QPushButton {\n"
" border: 2px solid whitesmoke;\n"
" border-radius: 5px;\n"
" background-color: rgb(255, 255, 135);\n"
"}\n"
"QPushButton:hover {\n"
" background-color: rgb(170, 170, 150);\n"
"}")

        self.verticalLayout.addWidget(self.b3)

        self.b1 = QPushButton(self.verticalLayoutWidget_2)
        self.b1.setObjectName(u"b1")
        self.b1.setStyleSheet(u"QPushButton {\n"
" border: 2px solid whitesmoke;\n"
" border-radius: 5px;\n"
" background-color: rgb(255, 255, 135);\n"
"}\n"
"QPushButton:hover {\n"
" background-color: rgb(170, 170, 150);\n"
"}")

        self.verticalLayout.addWidget(self.b1)

        self.b2 = QPushButton(self.verticalLayoutWidget_2)
        self.b2.setObjectName(u"b2")
        self.b2.setStyleSheet(u"QPushButton {\n"
" border: 2px solid whitesmoke;\n"
" border-radius: 5px;\n"
" background-color: rgb(255, 255, 135);\n"
"}\n"
"QPushButton:hover {\n"
" background-color: rgb(170, 170, 150);\n"
"}")

        self.verticalLayout.addWidget(self.b2)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 735, 22))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        self.menuEditar = QMenu(self.menubar)
        self.menuEditar.setObjectName(u"menuEditar")
        self.menuTareas = QMenu(self.menubar)
        self.menuTareas.setObjectName(u"menuTareas")
        self.menuOpciones = QMenu(self.menubar)
        self.menuOpciones.setObjectName(u"menuOpciones")
        self.menuMenu_Vertical = QMenu(self.menuOpciones)
        self.menuMenu_Vertical.setObjectName(u"menuMenu_Vertical")
        self.menuMenu_Horizontal = QMenu(self.menuOpciones)
        self.menuMenu_Horizontal.setObjectName(u"menuMenu_Horizontal")
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)
        self.toolBar_2 = QToolBar(MainWindow)
        self.toolBar_2.setObjectName(u"toolBar_2")
        MainWindow.addToolBar(Qt.LeftToolBarArea, self.toolBar_2)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuEditar.menuAction())
        self.menubar.addAction(self.menuTareas.menuAction())
        self.menubar.addAction(self.menuOpciones.menuAction())
        self.menuArchivo.addAction(self.actionNuevo_Archivo)
        self.menuArchivo.addAction(self.actionAbrir_Archivo)
        self.menuArchivo.addAction(self.actionGuardar)
        self.menuArchivo.addAction(self.actionGuardar_Como)
        self.menuEditar.addAction(self.actionCopiar)
        self.menuEditar.addAction(self.actionCortar)
        self.menuEditar.addAction(self.actionPegar)
        self.menuEditar.addAction(self.actionDeshacer)
        self.menuEditar.addAction(self.actionRehacer)
        self.menuTareas.addAction(self.actionNueva_Tarea)
        self.menuTareas.addAction(self.actionEliminar_Tarea)
        self.menuTareas.addAction(self.actionLimpiar)
        self.menuOpciones.addAction(self.menuMenu_Vertical.menuAction())
        self.menuOpciones.addAction(self.menuMenu_Horizontal.menuAction())
        self.menuMenu_Vertical.addAction(self.actionMostrar)
        self.menuMenu_Vertical.addAction(self.actionOcultar)
        self.menuMenu_Horizontal.addAction(self.actionMostrar_2)
        self.menuMenu_Horizontal.addAction(self.actionOcultar_2)
        self.toolBar.addAction(self.actionNueva_Tarea)
        self.toolBar.addAction(self.actionEliminar_Tarea)
        self.toolBar.addAction(self.actionGuardar)
        self.toolBar.addAction(self.actionCopiar)
        self.toolBar.addAction(self.actionCortar)
        self.toolBar.addAction(self.actionPegar)
        self.toolBar.addAction(self.actionDeshacer)
        self.toolBar.addAction(self.actionRehacer)
        self.toolBar.addAction(self.actionLimpiar)
        self.toolBar_2.addAction(self.actionLimpiar)
        self.toolBar_2.addAction(self.actionGuardar)

        self.retranslateUi(MainWindow)
        self.actionCopiar.triggered.connect(self.t2.copy)
        self.actionCortar.triggered.connect(self.t2.cut)
        self.actionPegar.triggered.connect(self.t2.paste)
        self.b3.clicked.connect(self.t2.clear)
        self.actionDeshacer.triggered.connect(self.t2.undo)
        self.actionRehacer.triggered.connect(self.t2.redo)
        self.actionLimpiar.triggered.connect(self.t2.clear)
        self.actionMostrar_2.triggered.connect(self.toolBar.show)
        self.actionMostrar.triggered.connect(self.toolBar_2.show)
        self.actionOcultar.triggered.connect(self.toolBar_2.hide)
        self.actionOcultar_2.triggered.connect(self.toolBar.hide)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionCopiar.setText(QCoreApplication.translate("MainWindow", u"Copiar", None))
#if QT_CONFIG(statustip)
        self.actionCopiar.setStatusTip(QCoreApplication.translate("MainWindow", u"Copias el texto seleccionado.", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.actionCopiar.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+C", None))
#endif // QT_CONFIG(shortcut)
        self.actionCortar.setText(QCoreApplication.translate("MainWindow", u"Cortar", None))
#if QT_CONFIG(statustip)
        self.actionCortar.setStatusTip(QCoreApplication.translate("MainWindow", u"Eliminas y copias el texto seleccionado.", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.actionCortar.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+X", None))
#endif // QT_CONFIG(shortcut)
        self.actionPegar.setText(QCoreApplication.translate("MainWindow", u"Pegar", None))
#if QT_CONFIG(statustip)
        self.actionPegar.setStatusTip(QCoreApplication.translate("MainWindow", u"Pegas el texto copiado.", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(shortcut)
        self.actionPegar.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+V", None))
#endif // QT_CONFIG(shortcut)
        self.actionNuevo_Archivo.setText(QCoreApplication.translate("MainWindow", u"Nuevo Archivo", None))
#if QT_CONFIG(shortcut)
        self.actionNuevo_Archivo.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+A", None))
#endif // QT_CONFIG(shortcut)
        self.actionAbrir_Archivo.setText(QCoreApplication.translate("MainWindow", u"Abrir Archivo", None))
#if QT_CONFIG(shortcut)
        self.actionAbrir_Archivo.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+A", None))
#endif // QT_CONFIG(shortcut)
        self.actionGuardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
#if QT_CONFIG(shortcut)
        self.actionGuardar.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionGuardar_Como.setText(QCoreApplication.translate("MainWindow", u"Guardar Como", None))
#if QT_CONFIG(shortcut)
        self.actionGuardar_Como.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionNueva_Tarea.setText(QCoreApplication.translate("MainWindow", u"Nueva Tarea", None))
#if QT_CONFIG(shortcut)
        self.actionNueva_Tarea.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+T", None))
#endif // QT_CONFIG(shortcut)
        self.actionEliminar_Tarea.setText(QCoreApplication.translate("MainWindow", u"Eliminar Tarea", None))
#if QT_CONFIG(shortcut)
        self.actionEliminar_Tarea.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+T", None))
#endif // QT_CONFIG(shortcut)
        self.actionDeshacer.setText(QCoreApplication.translate("MainWindow", u"Deshacer", None))
#if QT_CONFIG(shortcut)
        self.actionDeshacer.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Z", None))
#endif // QT_CONFIG(shortcut)
        self.actionRehacer.setText(QCoreApplication.translate("MainWindow", u"Rehacer", None))
#if QT_CONFIG(shortcut)
        self.actionRehacer.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Y", None))
#endif // QT_CONFIG(shortcut)
        self.actionLimpiar.setText(QCoreApplication.translate("MainWindow", u"Limpiar ", None))
#if QT_CONFIG(shortcut)
        self.actionLimpiar.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+L", None))
#endif // QT_CONFIG(shortcut)
        self.actionMostrar.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.actionOcultar.setText(QCoreApplication.translate("MainWindow", u"Ocultar", None))
        self.actionMostrar_2.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.actionOcultar_2.setText(QCoreApplication.translate("MainWindow", u"Ocultar", None))
        self.t2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Ink Free'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:9pt;\"><br /></p></body></html>", None))
        self.b3.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.b1.setText(QCoreApplication.translate("MainWindow", u"Nueva tarea", None))
        self.b2.setText(QCoreApplication.translate("MainWindow", u"Eliminar tarea", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
        self.menuEditar.setTitle(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.menuTareas.setTitle(QCoreApplication.translate("MainWindow", u"Tareas", None))
        self.menuOpciones.setTitle(QCoreApplication.translate("MainWindow", u"Opciones", None))
        self.menuMenu_Vertical.setTitle(QCoreApplication.translate("MainWindow", u"Menu Vertical", None))
        self.menuMenu_Horizontal.setTitle(QCoreApplication.translate("MainWindow", u"Menu Horizontal", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
        self.toolBar_2.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar_2", None))
    # retranslateUi


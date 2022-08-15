from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from main import *
from envego_banana import *
from . data_test import *

class MainFunction:
  def __init__(self, widgets: ViewControl):
    self.widgets = widgets
    self.widgets.scrollArea.hide()
    self.widgets.scrollArea_2.hide()
    self.widgets.scrollArea_3.hide()
    self.food_or_recipes = food_or_recipes

    self.widgets.editSearchBar.textChanged.connect(self.sync_search)
    self.widgets.buttonFood.clicked.connect(self.buttonFood_active)
    self.widgets.buttonRecipes.clicked.connect(self.buttonRecipes_active)
    self.widgets.buttonSearch.clicked.connect(self.buttonSearch_active)

    self.widgets.actionAbout.triggered.connect(self.actionAbout_clicked)
    self.widgets.pushButton.clicked.connect(self.banana)
  
  def sync_search(self):
    self.widgets.scrollArea.show()
    print(self.widgets.editSearchBar.text())
    if not self.widgets.editSearchBar.text():
      self.widgets.scrollArea.hide()
      self.widgets.scrollArea_2.hide()
      self.widgets.scrollArea_3.hide()
    elif self.widgets.editSearchBar.text() == "q":
      self.widgets.scrollArea.show()
      self.widgets.scrollArea_2.hide()
      self.widgets.scrollArea_3.hide()
    elif self.widgets.editSearchBar.text() == "qua t":
      self.widgets.scrollArea_2.show()
      self.widgets.scrollArea.hide()
      self.widgets.scrollArea_3.hide()
    elif self.widgets.editSearchBar.text() == "qua c":
      self.widgets.scrollArea_3.show()
      self.widgets.scrollArea_2.hide()
      self.widgets.scrollArea.hide()
  
  def buttonFood_active(self):
    self.food_or_recipes = False
    self.widgets.buttonFood.setStyleSheet("QPushButton{\n"
"  color: white;\n"
"  background-color: rgb(200, 153, 51);\n"
"  border: 0px solid;\n"
"  border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"  background-color: rgb(56, 56, 56);\n"
"}")

  def buttonRecipes_active(self):
    self.food_or_recipes = True
    self.widgets.buttonRecipes.setStyleSheet("QPushButton{\n"
"  color: white;\n"
"  background-color: rgb(200, 153, 51);\n"
"  border: 0px solid;\n"
"  border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"  background-color: rgb(56, 56, 56);\n"
"}")

  def buttonSearch_active(self):
    pass

  def actionAbout_clicked(self):
    self.widgets.stackedWidget.setCurrentIndex(1)

  def banana(self):
    self.BANANA = BANANA(self)
    self.BANANA.exec()
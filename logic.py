import math
import os
from PyQt6.QtWidgets import *
from gui import *

class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.hide_area()
        self.enable_top('Side')

        self.Button_zero.clicked.connect(lambda : self.on_button_clicked())
        self.Button_one.clicked.connect(lambda: self.on_button_clicked())
        self.Button_two.clicked.connect(lambda: self.on_button_clicked())
        self.Button_three.clicked.connect(lambda: self.on_button_clicked())
        self.Button_four.clicked.connect(lambda: self.on_button_clicked())
        self.Button_five.clicked.connect(lambda: self.on_button_clicked())
        self.Button_six.clicked.connect(lambda: self.on_button_clicked())
        self.Button_seven.clicked.connect(lambda: self.on_button_clicked())
        self.Button_eight.clicked.connect(lambda: self.on_button_clicked())
        self.Button_nine.clicked.connect(lambda: self.on_button_clicked())
        self.Button_equal.clicked.connect(lambda: self.on_button_clicked())
        self.Button_add.clicked.connect(lambda: self.on_button_clicked())
        self.Button_subtract.clicked.connect(lambda: self.on_button_clicked())
        self.Button_multiply.clicked.connect(lambda: self.on_button_clicked())
        self.Button_divide.clicked.connect(lambda: self.on_button_clicked())
        self.Button_decimal.clicked.connect(lambda: self.on_button_clicked())
        self.Button_clear.clicked.connect(lambda: self.on_button_clicked())
        self.Button_negative.clicked.connect(lambda: self.on_button_clicked())
        self.Button_delete.clicked.connect(lambda: self.on_button_clicked())
        self.Button_history.clicked.connect(lambda: self.on_button_clicked())

        self.Button_top.clicked.connect(lambda: self.input_top())
        self.Button_middle.clicked.connect(lambda: self.input_middle())
        self.Button_bottom.clicked.connect(lambda: self.input_bottom())
        self.Button_top_clear.clicked.connect(lambda: self.clear_top())
        self.Button_middle_clear.clicked.connect(lambda: self.clear_middle())
        self.Button_bottom_clear.clicked.connect(lambda: self.clear_bottom())

        self.Radio_square.clicked.connect(lambda: self.shape_clicked())
        self.Radio_rectangle.clicked.connect(lambda: self.shape_clicked())
        self.Radio_circle.clicked.connect(lambda: self.shape_clicked())
        self.Radio_triangle.clicked.connect(lambda: self.shape_clicked())
        self.Radio_trapezoid.clicked.connect(lambda: self.shape_clicked())

    def on_button_clicked(self):
        button = self.sender()
        current_text = self.Display.text()

        if 'Error' in current_text:
            current_text = ''

        if current_text == '0':
            current_text = ''

        if button.text() == '=':
            try:
                f = open("history.txt", "a")
                if self.Radio_square.isChecked() and self.Input_top.text() != '':
                    result = float(self.Input_top.text()) ** 2
                    f.write("Square: Sides - " + str(self.input_top()) + ' = ' + str(result) + '\n')
                    self.Display.setText(str(result))
                elif self.Radio_rectangle.isChecked() and self.Input_top.text() != '' and self.Input_middle.text() != '':
                    result = float(self.Input_top.text()) * float(self.Input_middle.text())
                    f.write("Rectangle: Sides - " + str(self.Input_top.text()) + ' and ' + str(self.Input_middle.text()) + ' = ' + str(result) + '\n')
                    self.Display.setText(str(result))
                elif self.Radio_circle.isChecked() and self.Input_top.text() != '':
                    result = math.pi * (float(self.Input_top.text()) ** 2)
                    f.write("Circle: Radius - " + str(self.Input_top.text()) + ' = ' + str(result) + '\n')
                    self.Display.setText(str(result))
                elif self.Radio_triangle.isChecked() and self.Input_top.text() != '' and self.Input_middle.text() != '':
                    result = .5 * float(self.Input_top.text()) * float(self.Input_middle.text())
                    f.write("Triangle: Base - " + str(self.Input_top.text()) + ' Height - ' + str(self.Input_middle.text()) + ' = ' + str(result) + '\n')
                    self.Display.setText(str(result))
                elif self.Radio_trapezoid.isChecked() and self.Input_top.text() != '' and self.Input_middle.text() != '' and self.Input_bottom.text() != '':
                    result = ((float(self.Input_top.text()) + float(self.Input_middle.text())) / 2) * float(self.Input_bottom.text())
                    f.write("Trapezoid: Bases - " + str(self.Input_top.text()) + ' and ' + str(self.Input_middle.text()) + ' Height - ' + str(self.Input_bottom.text()) + ' = ' + str(result) + '\n')
                    self.Display.setText(str(result))

                else:
                    result = str(eval(current_text))
                    f.write("Calculator: " + str(self.Display.text()) + '=' + result + '\n')
                    self.Display.setText(result)

                f.close()

            except ZeroDivisionError:
                self.Display.setText("Invalid")
            except:
                self.Display.setText("Invalid")

        elif button.text() == 'DEL':
            try:
                self.delete_last()
                if self.Display.text() == '':
                    self.Display.setText('0')

            except:
                pass

        elif button.text() == '+/-':
            try:
                if self.Display.text()[-1] == '-':
                    self.delete_last()
                else:
                    self.Display.setText(current_text + '-')

            except:
                pass

        elif button.text() == 'History':
            os.startfile('file.txt')  # Note: unable to test if this works on non-windows systems


        elif button.text() == 'C':
            self.Display.setText('0')

        else:
            self.Display.setText(current_text + button.text())



    def shape_clicked(self):
        if self.Radio_square.isChecked():
            self.enable_top("Side")
            self.disable_middle()
            self.disable_bottom()
        elif self.Radio_rectangle.isChecked():
            self.enable_top("Length")
            self.enable_middle("Width")
            self.disable_bottom()
        elif self.Radio_circle.isChecked():
            self.enable_top("Radius")
            self.disable_middle()
            self.disable_bottom()
        elif self.Radio_triangle.isChecked():
            self.enable_top("Base")
            self.enable_middle("Height")
            self.disable_bottom()
        elif self.Radio_trapezoid.isChecked():
            self.enable_top("Base 1")
            self.enable_middle("Base 2")
            self.enable_bottom("Height")


    def hide_area(self):
        self.Input_top.hide()
        self.Input_middle.hide()
        self.Input_bottom.hide()
        self.Button_top_clear.hide()
        self.Button_middle_clear.hide()
        self.Button_bottom_clear.hide()
        self.Button_top.hide()
        self.Button_middle.hide()
        self.Button_bottom.hide()

    def delete_last(self):
        text = self.Display.text()
        text = text[:-1]
        self.Display.setText(text)

    def enable_top(self, text: str):
        self.Input_top.show()
        self.Button_top.show()
        self.Button_top_clear.show()
        self.Label_top.setText(text)

    def disable_top(self):
        self.Input_top.hide()
        self.Button_top.hide()
        self.Button_top_clear.hide()
        self.Label_top.setText('')

    def enable_middle(self, text: str):
        self.Input_middle.show()
        self.Button_middle.show()
        self.Button_middle_clear.show()
        self.Label_middle.setText(text)

    def disable_middle(self):
        self.Input_middle.hide()
        self.Button_middle.hide()
        self.Button_middle_clear.hide()
        self.Label_middle.setText('')

    def enable_bottom(self, text: str):
        self.Input_bottom.show()
        self.Button_bottom.show()
        self.Button_bottom_clear.show()
        self.Label_bottom.setText(text)

    def disable_bottom(self):
        self.Input_bottom.hide()
        self.Button_bottom.hide()
        self.Button_bottom_clear.hide()
        self.Label_bottom.setText('')

    def input_top(self):
        try:
            num = self.Display.text()
            self.Input_top.setText(num)

        except:
            pass

    def clear_top(self):
        self.Input_top.setText('')

    def input_middle(self):
        try:
            num = self.Display.text()
            self.Input_middle.setText(num)

        except:
            pass

    def clear_middle(self):
        self.Input_middle.setText('')

    def input_bottom(self):
        try:
            num = self.Display.text()
            self.Input_bottom.setText(num)

        except:
            pass

    def clear_bottom(self):
        self.Input_bottom.setText('')

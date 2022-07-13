from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout
from PyQt6.QtWidgets import  QLabel, QPushButton, QLineEdit, QComboBox
from PyQt6.QtCore import Qt    # qt= aliniere
from bs4 import BeautifulSoup
import requests

def get_currency(in_currency, out_currency):
    url = f"https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1"
    content = requests.get(url).text
    soup = BeautifulSoup(content, "html.parser")
    rate = soup.find("span", class_="ccOutputRslt").get_text()
    rate = float(rate[0:-4])
    return rate

def show_currecy():
    input_text = float(text.text())
    in_cur= in_combo.currentText()
    target_cur= target_combo.currentText()
    rate= get_currency(in_cur, target_cur)
    output = round(input_text * rate, 2)
    message= f"{input_text} {in_cur} is {output} {target_cur}"  #------combo1
    output_label.setText(str(message))              #----layout2-------combo2
                                #layout---layout1--------layout3-------input
                                 #     ---label                 -------button
app= QApplication([])
window= QWidget()
window.setWindowTitle("Currency Converter")

layout= QVBoxLayout()
layout1= QHBoxLayout()
layout.addLayout(layout1)

output_label= QLabel("")
layout.addWidget(output_label)

layout2= QVBoxLayout()
layout1.addLayout(layout2)

layout3= QVBoxLayout()
layout1.addLayout(layout3)

in_combo= QComboBox()
currencies= ["USD", "EUR","INR","RON"]
in_combo.addItems(currencies)
layout2.addWidget(in_combo)

target_combo= QComboBox()
target_combo.addItems(currencies)
layout2.addWidget(target_combo)

text= QLineEdit()
layout3.addWidget(text)

btn= QPushButton("Convert!")
layout3.addWidget(btn, alignment=Qt.AlignmentFlag.AlignBottom)   # qt folosit
btn.clicked.connect(show_currecy)

window.setLayout(layout)
window.show()
app.exec()

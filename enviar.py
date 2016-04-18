import sys
from PyQt4.QtCore import pyqtSlot
from PyQt4.QtGui import *
import telegram
 
# create our window
app = QApplication(sys.argv)
w = QWidget()
w.setWindowTitle('Send a message')
 
# Create textbox
textbox = QTextEdit(w)
textbox.move(20, 20)
textbox.resize(600,240)
 
# Set window size. 
w.resize(640, 300)
 
# Create a button in the window
button = QPushButton('Send', w)
button.move(550,260)
 
# Create the actions 
@pyqtSlot()
def on_click():
    bot = telegram.Bot(token='213083457:AAGxNQvchf8Q_SpgvGhQrJlFMo7MaX9Mf64')
    chat_id = bot.getUpdates()[-1].message.chat_id
    bot.sendMessage(chat_id=chat_id, text=str(textbox.toPlainText()))
 
# connect the signals to the slots
button.clicked.connect(on_click)
 
# Show the window and run the app
w.show()
app.exec_()
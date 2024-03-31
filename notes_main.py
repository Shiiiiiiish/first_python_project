from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QCheckBox, QHBoxLayout,QListWidget,QLineEdit,QTextEdit,QInputDialog
import json


# notes = {
#     "Названия заметки" :
#     {
#         "текст" : "Солнечная система",
#         "теги" : ["солнечная система"]
#     },
#     "Название заметки1" :
#     {
#         "текст" : "Математика, химия, русский язык",
#         "теги" : ["уроки"]
#     }
# }


# with open('notes_data.json', 'w', encoding='utf-8') as file:
#     json.dump(notes, file)







app = QApplication([])
win  = QWidget()

#виджеты
#правая часть
l1 = QLabel('Список заметок')
lw1 = QListWidget()
create = QPushButton('создать заметку')
remove = QPushButton('удалить заметку')
save = QPushButton('сохранить заметку')
l2 = QLabel('Список тегов:')
lw2 = QListWidget()
lin = QLineEdit('Введите тег.....')
add = QPushButton('добавить к заметке')
otk = QPushButton('открепить от заметки')
search = QPushButton('Искать заметки по тегу:')
#левая часть
text = QTextEdit()


#лайауты
lay_left = QVBoxLayout()
lay_right = QVBoxLayout()
h_lay = QHBoxLayout()
h3 = QHBoxLayout()
h4 = QHBoxLayout()

#размещение лайаутов
win.setLayout(h_lay)
h_lay.addLayout(lay_left)
h_lay.addLayout(lay_right)



#виджеты на лайауты
lay_left.addWidget(text)
lay_right.addWidget(l1)
lay_right.addWidget(lw1)
h3.addWidget(create)
h3.addWidget(remove)
lay_right.addLayout(h3)
lay_right.addWidget(save)
lay_right.addWidget(l2)
lay_right.addWidget(lw2)
lay_right.addWidget(lin)
lay_right.addLayout(h4)
h4.addWidget(add)
h4.addWidget(otk)
lay_right.addWidget(search)

def show_note():
    name = lw1.selectedItems()[0].text()
    text.setText(notes[name]['текст'])
    lw2.clear()                                                                                      
    lw2.addItems(notes[name]['теги'])
lw1.itemClicked.connect(show_note)


def add_note():
    note_name, ok = QInputDialog.getText(win, 'добавить заметку', 'название заметки')
    if ok and note_name != '':
        notes[note_name] = {'текст':'', 'теги':[]}
        lw1.addItem(note_name)

create.clicked.connect(add_note)

def delete():
    if lw1.selectedItems():
        name = lw1.selectedItems()[0].text()
        del notes[name]
        text.clear()
        lw1.clear()
        lw2.clear()
        lw1.addItems(notes)
        with open('notes_data.json', 'w', encoding='utf-8') as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)
    else:
        print('заметка для удаления не выбрана!!!!!')


def save_note():
    if lw1.selectedItems():
        name = lw1.selectedItems()[0].text()
        notes[name]['текст'] = text.toPlainText()
        with open('notes_data.json', 'w', encoding='utf-8') as file:
            json.dump(notes, file)
    else:
        print('заметка не выбрана!')


def add_tag():
    if lw1.selectedItems():
        name1 = lw1.selectedItems()[0].text()
        name = lin.text()
        if not name in notes[name1]['теги']:
            notes[name1]['теги'].append(name)
            lw2.addItem(name)
            lin.clear()
            with open('notes_data.json', 'w', encoding='utf-8') as file:
                json.dump(notes, file)


def del_tag():
    if lw1.selectedItems():
        name = lw2.selectedItems()[0].text()
        nz = lw1.selectedItems()[0].text()
        notes[nz]['теги'].remove(name)
        lw2.clear()
        lw2.addItems(notes[nz]['теги'])
        with open('notes_data.json', 'w', encoding='utf-8') as file:
            json.dump(notes, file)
    else:
        print('заметка для удаления тега не выбрана')


def search_note():
    if search.text() == 'Искать заметки по тегу:':
        notes_filtered = {}
        tag = lin.text()
        for name in notes:
            if tag in notes[name]['теги']:
                notes_filtered[name] = notes[name]
        search.setText('Сбросить поиск')
        lw1.clear()
        lw2.clear()
        lw1.addItems(notes_filtered)
    elif search.text() == 'Сбросить поиск':
        lw1.clear()
        lw2.clear()
        lw1.addItems(notes)







lw1.setStyleSheet('color: #FFFFFF;background-color: #262626;selection-background-color: #8B0000;border-radius: 5px')
text.setStyleSheet('color: #FFFFFF;background-color: #262626;border-radius: 5px')
create.setStyleSheet('background-color: #8B0000;border-style: outset;border-width: 4px;border-color: #000000; border-radius: 10px;font: bold 14px;min-width: 10em;padding: 4px;color: #FFFFFF')
save.setStyleSheet('background-color: #8B0000;border-style: outset;border-width: 4px;border-color: #000000; border-radius: 10px;font: bold 14px;min-width: 10em;padding: 4px;color: #FFFFFF')
remove.setStyleSheet('background-color: #8B0000;border-style: outset;border-width: 4px;border-color: #000000; border-radius: 10px;font: bold 14px;min-width: 10em;padding: 4px;color: #FFFFFF')
save.clicked.connect(save_note)
add.setStyleSheet('background-color: #8B0000;border-style: outset;border-width: 4px;border-color: #000000; border-radius: 10px;font: bold 14px;min-width: 10em;padding: 4px;color: #FFFFFF')
otk.setStyleSheet('background-color: #8B0000;border-style: outset;border-width: 4px;border-color: #000000; border-radius: 10px;font: bold 14px;min-width: 10em;padding: 4px;color: #FFFFFF')
search.setStyleSheet('background-color: #8B0000;border-style: outset;border-width: 4px;border-color: #000000; border-radius: 10px;font: bold 14px;min-width: 10em;padding: 4px;color: #FFFFFF')
lw2.setStyleSheet('color: #FFFFFF;background-color: #262626;selection-background-color: #8B0000;border-radius: 5px')
lin.setStyleSheet('color: #FFFFFF;background-color: #262626;border-radius: 5px')
l1.setStyleSheet('color: #FFFFFF;font: bold 10px')
l2.setStyleSheet('color: #FFFFFF;font: bold 10px')
win.setStyleSheet('background-color: #000000')
app.setStyleSheet('background-color: #000000')
    

    


search.clicked.connect(search_note)
otk.clicked.connect(del_tag)
add.clicked.connect(add_tag)
save.clicked.connect(save_note)



remove.clicked.connect(delete)


win.setWindowTitle('умные заметки')
win.resize(1000, 700)
win.show()

with open('notes_data.json', 'r', encoding='utf-8') as file:
    notes = json.load(file)

lw1.addItems(notes)


app.exec_()
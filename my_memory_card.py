from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QRadioButton, QGroupBox, QVBoxLayout, QHBoxLayout, QButtonGroup
from random import shuffle, randint

app = QApplication([])
main_win = QWidget()


class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

questions_list = []
q1 = Question('Государственный язык Бразилии','Португальский','Испанский','Итальянский','Бразильский')
questions_list.append(q1)
q2 = Question('Какого цвета нет на флаге России?','Зелёный','Красный','Белый','Синий')
questions_list.append(q2)
q3 = Question('Национальная хижина якутов','Ураса','Юрта','Иглу','Хата')
questions_list.append(q3)
q4 = Question('Столица России','Москва','Екатеринбург','Омск','Саратов')
questions_list.append(q4)
q5 = Question('Предыдущая столица России','Санкт-Петербург','Москва','Ростов','Тула')
questions_list.append(q5)
q6 = Question('Кто/что больше всех?','Антон','Муравей','Инфузория туфелька','Синий кит')
questions_list.append(q6)
q7 = Question('Самый большой континент','Евразия','Австралия','Африка','Антарктида')
questions_list.append(q7)
q8 = Question('Столица Великобритании','Лондон','Нью-йорк','Техас','Омск')
questions_list.append(q8)
q9 = Question('Какой средний вес облака?','500т','5кг','1т','1гр')
questions_list.append(q9)
q10 = Question('За сколько свет от солнца доходит до нас?','8.5мин','1сек','1час','Моментально')
questions_list.append(q10)

main_win.resize(400,200)
main_win.setWindowTitle('Memory Card')
vopros = QLabel('Какой национальности не существует?')
r1 = QRadioButton('Энцы')
r2 = QRadioButton('Чулымцы')
r3 = QRadioButton('Смурфы')
r4 = QRadioButton('Алеуты')
Radio = QGroupBox('Варианты')
otvet = QPushButton('Ответить')

RadioGroup = QButtonGroup()
RadioGroup.addButton(r1)
RadioGroup.addButton(r2)
RadioGroup.addButton(r3)
RadioGroup.addButton(r4)

line1 = QHBoxLayout()
line2 = QVBoxLayout()
line3 = QVBoxLayout()
line4 = QVBoxLayout()
line5 = QHBoxLayout()
line6 = QHBoxLayout()
line8 = QVBoxLayout()
line7 = QVBoxLayout()
line4.addWidget(vopros,alignment = Qt.AlignCenter)
line4.addWidget(Radio)
Radio.setLayout(line1)
line1.addLayout(line2)
line1.addLayout(line3)

line2.addWidget(r1,alignment = Qt.AlignCenter)
line2.addWidget(r3,alignment = Qt.AlignCenter)
line3.addWidget(r2,alignment = Qt.AlignCenter)
line3.addWidget(r4,alignment = Qt.AlignCenter)

Radio1 = QGroupBox('Результат теста')
prawotvet = QLabel('Правильный ответ')
praw = QLabel('Правильно/Неправильно')
line4.addWidget(Radio1)
Radio1.setLayout(line8)
line8.addLayout(line5)
line8.addLayout(line6)
line5.addLayout(line7)
line6.addWidget(prawotvet,alignment = Qt.AlignCenter)
line7.addWidget(praw,alignment = Qt.AlignLeft)
line4.addWidget(otvet,alignment = Qt.AlignCenter)
line4.addWidget(otvet,alignment = Qt.AlignCenter)
Radio1.hide()
main_win.setLayout(line4)

def show_result():
    Radio.hide()
    Radio1.show()
    otvet.setText('Следующий вопрос')

def show_question():
    RadioGroup.setExclusive(False)
    r1.setChecked(False)
    r2.setChecked(False)
    r3.setChecked(False)
    r4.setChecked(False)
    RadioGroup.setExclusive(True)
    Radio.show()
    Radio1.hide()
    otvet.setText('Ответить')

answers = [r1,r2,r3,r4]

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    vopros.setText(q.question)
    prawotvet.setText(q.right_answer)
    show_question()

def show_correct(res):
    praw.setText(res)
    show_result()

main_win.score = 0
def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно')
        main_win.score += 1
    else:
        show_correct('Неверно!')
main_win.total = 0
main_win.cur_question = -1
def next_question():
    main_win.total += 1
    main_win.cur_question = randint(1,len(questions_list))
    if main_win.cur_question >= len(questions_list):
        main_win.cur_question = 0
    ask(questions_list[main_win.cur_question])

total = 0
def click_OK():
    if otvet.text() == 'Ответить':
        check_answer()
        print('Статистика')
        print('-Всего вопросов:',main_win.total)
        print('-Правильных ответов:',main_win.score)
        print('Рейтинг:',main_win.score/main_win.total*100,'%')
    else:
        next_question()

def start_test():
    if otvet.text() == 'Ответить':
        show_result()
    else:
        show_question()




otvet.clicked.connect(click_OK)  

next_question()


main_win.show()
app.exec_()



import math
from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib.pyplot as plt
import numpy as np
from PyQt5.QtWidgets import QMessageBox, QApplication
from PyQt5.QtGui import QIcon
def sin_taylor(x, terms):
    x_normalized = x % (2 * math.pi)
    sin_approximation = 0
    coefficients_sin = []
    for n in range(terms):
        sign = (-1) ** n
        term = sign * (x_normalized ** (2 * n + 1)) / math.factorial(2 * n + 1)
        sin_approximation += term
        coefficients_sin.append(term)
    return sin_approximation, coefficients_sin

def cos_taylor(x, terms):
    x_normalized = x % (2 * math.pi)
    cos_approximation = 0
    coefficients_cos = []
    for n in range(terms):
        sign = (-1) ** n
        term = sign * (x_normalized ** (2 * n)) / math.factorial(2 * n)
        cos_approximation += term
        coefficients_cos.append(term)
    return cos_approximation, coefficients_cos

def tg_taylor(x, terms):
    sin_value, sin_coefficients = sin_taylor(x, terms)
    cos_value, cos_coefficients = cos_taylor(x, terms)

    tg_approximation = sin_value / cos_value
    tg_coefficients = []

    for i in range(len(sin_coefficients)):
        tg_coefficients.append(sin_coefficients[i] / cos_coefficients[i])

    return tg_approximation, tg_coefficients

def ctg_taylor(x, terms):
    sin_value, sin_coefficients = sin_taylor(x, terms)
    cos_value, cos_coefficients = cos_taylor(x, terms)

    ctg_approximation = cos_value / sin_value
    ctg_coefficients = []

    for i in range(len(cos_coefficients)):
        ctg_coefficients.append(cos_coefficients[i] / sin_coefficients[i])

    return ctg_approximation, ctg_coefficients

class Ui_Taylor_series(object):
    def setupUi(self, Taylor_series):
        help_action = QtWidgets.QAction("Справка", Taylor_series)
        help_action.triggered.connect(self.show_help)
        menu_bar = Taylor_series.menuBar()
        menu_bar.addAction(help_action)
        menu_bar.setStyleSheet("font: 75 10pt \"arial\"; color: rgb(206, 129, 76); background-color: rgb(43, 45, 48);")
        Taylor_series.setObjectName("Taylor_series")
        Taylor_series.resize(907, 573)
        Taylor_series.setAccessibleName("")
        Taylor_series.setStyleSheet("font: 75 10pt \"Times New Roman\";\n""background-color: rgb(43, 45, 48);")
        icon = QtGui.QIcon(r"D:\BGAS_study\Python\kurss\.idea\icon_for_taylor.png")
        Taylor_series.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(Taylor_series)
        self.centralwidget.setStyleSheet("font: 10pt \"Arial\";")
        self.centralwidget.setObjectName("centralwidget")
        self.raschet = QtWidgets.QPushButton(self.centralwidget)
        self.raschet.setGeometry(QtCore.QRect(60, 320, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.raschet.setFont(font)
        self.raschet.setStyleSheet("color: rgb(100, 170, 102);")
        self.raschet.setObjectName("raschet")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(30, 20, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_1.setFont(font)
        self.label_1.setStyleSheet("color: rgb(106, 171, 115);")
        self.label_1.setObjectName("label_1")
        self.functions = QtWidgets.QGroupBox(self.centralwidget)
        self.functions.setGeometry(QtCore.QRect(20, 160, 200, 100))
        self.functions.setStyleSheet("font: 75 10pt \"Times New Roman\";\n"
                                     "color: rgb(206, 129, 76);")
        self.functions.setObjectName("functions")
        self.func_sinx = QtWidgets.QCheckBox(self.functions)
        self.func_sinx.setGeometry(QtCore.QRect(20, 30, 101, 20))
        self.func_sinx.setStyleSheet("color: rgb(86, 168, 245);\n"
                                     "")
        self.func_sinx.setObjectName("func_sinx")
        self.func_cosx = QtWidgets.QCheckBox(self.functions)
        self.func_cosx.setGeometry(QtCore.QRect(20, 60, 101, 20))
        self.func_cosx.setStyleSheet("color: rgb(86, 168, 245);")
        self.func_cosx.setObjectName("func_cosx")
        self.func_tgx = QtWidgets.QCheckBox(self.functions)
        self.func_tgx.setGeometry(QtCore.QRect(110, 30, 71, 20))
        self.func_tgx.setStyleSheet("color: rgb(86, 168, 245);\n"
                                    "")
        self.func_tgx.setObjectName("func_tgx")
        self.func_ctgx = QtWidgets.QCheckBox(self.functions)
        self.func_ctgx.setGeometry(QtCore.QRect(110, 60, 71, 20))
        self.func_ctgx.setStyleSheet("color: rgb(86, 168, 245);\n"
                                     "")
        self.func_ctgx.setObjectName("func_ctgx")
        self.vivod_isledovania = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.vivod_isledovania.setGeometry(QtCore.QRect(260, 40, 601, 501))
        self.vivod_isledovania.setStyleSheet("color: rgb(188, 190, 196);")
        self.vivod_isledovania.setObjectName("vivod_isledovania")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(260, 10, 231, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(106, 171, 115);")
        self.label_2.setObjectName("label_2")
        self.znachenie_x = QtWidgets.QLineEdit(self.centralwidget)
        self.znachenie_x.setGeometry(QtCore.QRect(60, 120, 113, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.znachenie_x.setFont(font)
        self.znachenie_x.setStyleSheet("color: rgb(188, 190, 196);")
        self.znachenie_x.setObjectName("znachenie_x")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 90, 201, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(106, 171, 115);")
        self.label_3.setObjectName("label_3")
        self.clean = QtWidgets.QPushButton(self.centralwidget)
        self.clean.setGeometry(QtCore.QRect(60, 370, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.clean.setFont(font)
        self.clean.setStyleSheet("color: rgb(206, 129, 76);")
        self.clean.setObjectName("clean")
        self.graph = QtWidgets.QPushButton(self.centralwidget)
        self.graph.setGeometry(QtCore.QRect(50, 420, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.graph.setFont(font)
        self.graph.setStyleSheet("color: rgb(100, 170, 102);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(r"D:\BGAS_study\Python\kurss\.idea\graph_icon.png"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        self.graph.setIcon(icon)
        self.graph.setIconSize(QtCore.QSize(30, 30))
        self.graph.setObjectName("graph")
        self.tochnost_razlojenia = QtWidgets.QComboBox(self.centralwidget)
        self.tochnost_razlojenia.setGeometry(QtCore.QRect(70, 50, 111, 22))
        self.tochnost_razlojenia.setStyleSheet("color: rgb(188, 190, 196);")
        self.tochnost_razlojenia.setObjectName("tochnost_razlojenia")
        self.tochnost_razlojenia.addItem("")
        self.tochnost_razlojenia.addItem("")
        self.tochnost_razlojenia.addItem("")
        self.tochnost_razlojenia.addItem("")
        self.tochnost_razlojenia.addItem("")
        self.tochnost_razlojenia.addItem("")
        self.tochnost_razlojenia.addItem("")
        self.tochnost_razlojenia.addItem("")
        self.tochnost_razlojenia.addItem("")
        self.tochnost_razlojenia.addItem("")
        Taylor_series.setCentralWidget(self.centralwidget)

        self.retranslateUi(Taylor_series)
        QtCore.QMetaObject.connectSlotsByName(Taylor_series)
        self.raschet.clicked.connect(self.calculate_and_display)
        self.clean.clicked.connect(self.clear_output)
        self.graph.clicked.connect(self.plot_graphs)

    def show_help(self):
        help_text = """
        <h2 style="text-align: center;">Справка по приложению "Разложение функции в ряд Тейлора"</h2>

        <h3>Использование:</h3>

        <ol>
        <li><strong>Выбор функций для разложения:</strong> Выберите одну или несколько функций для разложения, установив флажки напротив соответствующих названий функций.</li>
        <li><strong>Задание точности разложения:</strong> Выберите желаемое количество членов ряда Тейлора для аппроксимации функции.</li>
        <li><strong>Ввод значения x:</strong> Введите значение аргумента x в радианах для вычисления функций.</li>
        <li><strong>Нажмите кнопку "Рассчитать":</strong> После ввода значений и выбора параметров нажмите кнопку "Рассчитать", чтобы выполнить расчет и отобразить результаты.</li>
        <li><strong>Анализ результатов:</strong> После выполнения расчета результаты будут отображены в текстовом поле справа. Вы также получите информацию о точности аппроксимации и сходимости рядов.</li>
        <li><strong>Очистка результатов:</strong> Для очистки вывода нажмите кнопку "Очистить".</li>
        <li><strong>Вывод графиков:</strong> Нажмите кнопку "Вывести график", чтобы построить графики точных значений функций и их аппроксимаций.</li>
        <li><strong>Справка:</strong> Для получения дополнительной информации о функциональности приложения нажмите на пункт "Справка" в меню и прочитайте описание.</li>
        </ol>
        """
        help_window = QtWidgets.QMessageBox()
        help_window.setText(help_text)
        help_window.setWindowTitle("Справка")
        help_window.setStyleSheet("font: 75 10pt \"arial\"; color: rgb(188, 190, 196); background-color: rgb(43, 45, 48);")
        help_window.exec_()
    def retranslateUi(self, Taylor_series):
        _translate = QtCore.QCoreApplication.translate
        Taylor_series.setWindowTitle(_translate("Taylor_series", "Разложение функции в ряд Тейлора"))
        self.raschet.setText(_translate("Taylor_series", "Рассчитать"))
        self.label_1.setText(_translate("Taylor_series", "Точность разложения:"))
        self.functions.setTitle(_translate("Taylor_series", "Функции для разложения"))
        self.func_sinx.setText(_translate("Taylor_series", "sin(x)"))
        self.func_cosx.setText(_translate("Taylor_series", "cos(x)"))
        self.func_tgx.setText(_translate("Taylor_series", "tg(x)"))
        self.func_ctgx.setText(_translate("Taylor_series", "ctg(x)"))
        self.label_2.setText(_translate("Taylor_series", "Коэффициенты разложения:"))
        self.label_3.setText(_translate("Taylor_series", "Значение x (в радианах):"))
        self.clean.setText(_translate("Taylor_series", "Очистить"))
        self.graph.setText(_translate("Taylor_series", "Вывести\n"
                                                       " график"))
        self.tochnost_razlojenia.setWhatsThis(
            _translate("Taylor_series", "<html><head/><body><p>фывфывф</p></body></html>"))
        self.tochnost_razlojenia.setItemText(0, _translate("Taylor_series", "1"))
        self.tochnost_razlojenia.setItemText(1, _translate("Taylor_series", "2"))
        self.tochnost_razlojenia.setItemText(2, _translate("Taylor_series", "3"))
        self.tochnost_razlojenia.setItemText(3, _translate("Taylor_series", "4"))
        self.tochnost_razlojenia.setItemText(4, _translate("Taylor_series", "5"))
        self.tochnost_razlojenia.setItemText(5, _translate("Taylor_series", "6"))
        self.tochnost_razlojenia.setItemText(6, _translate("Taylor_series", "7"))
        self.tochnost_razlojenia.setItemText(7, _translate("Taylor_series", "8"))
        self.tochnost_razlojenia.setItemText(8, _translate("Taylor_series", "9"))
        self.tochnost_razlojenia.setItemText(9, _translate("Taylor_series", "10"))

    def calculate_and_display(self):
        try:
            terms = int(self.tochnost_razlojenia.currentText())
            x = float(self.znachenie_x.text())
            if self.func_sinx.isChecked():
                sin_approximation, coefficients_sin = sin_taylor(x, terms)
                exact_value = math.sin(x)
                if math.sin(x) == 0:
                    raise Exception("Некорректное значение sin(x), введите не нулевое число!")
                self.display_result("sin(x)", sin_approximation, exact_value, coefficients_sin)
                self.display_convergence([(sin_approximation, exact_value)])

            if self.func_cosx.isChecked():
                cos_approximation, coefficients_cos = cos_taylor(x, terms)
                exact_value = math.cos(x)
                self.display_result("cos(x)", cos_approximation, exact_value, coefficients_cos)
                self.display_convergence([(cos_approximation, exact_value)])

            if self.func_tgx.isChecked():
                tg_approximation, coefficients_tg = tg_taylor(x, terms)
                exact_value = math.tan(x)
                if exact_value == 0:
                    raise Exception("Тангенс не может быть вычислен для угла, при котором катет равен 0!")
                self.display_result("tg(x)", tg_approximation, exact_value, coefficients_tg)
                self.display_convergence([(tg_approximation, exact_value)])

            if self.func_ctgx.isChecked():
                ctg_approximation, coefficients_ctg = ctg_taylor(x, terms)
                exact_value = 1 / math.tan(x)
                self.display_result("ctg(x)", ctg_approximation, exact_value, coefficients_ctg)
                self.display_convergence([(ctg_approximation, exact_value)])

        except ValueError as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Неверный формат. Пожалуйста введите число!")
            msg.setWindowTitle("Ошибка")
            msg.setStyleSheet("QMessageBox { background-color: rgb(43, 45, 48); }"
                              "QMessageBox QLabel { color: rgb(188, 190, 196); font-size: 12pt; font-family: Times New Roman; }")
            msg.exec_()
        except ZeroDivisionError:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Котангенс не может быть вычислен для угла, при котором катет равен 0!")
            msg.setWindowTitle("Ошибка")
            msg.setStyleSheet("QMessageBox { background-color: rgb(43, 45, 48); }"
                              "QMessageBox QLabel { color: rgb(188, 190, 196); font-size: 12pt; font-family: Times New Roman; }")
            msg.exec_()
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText(str(e.args[0]))
            msg.setWindowTitle("Ошибка")
            msg.setStyleSheet("QMessageBox { background-color: rgb(43, 45, 48); }"
                              "QMessageBox QLabel { color: rgb(188, 190, 196); font-size: 12pt; font-family: Times New Roman; }")
            msg.exec_()

    def display_result(self, function_name, approximation, exact_value, coefficients):
        self.vivod_isledovania.appendPlainText(f"Приближенное значение {function_name}: {approximation}")
        self.vivod_isledovania.appendPlainText(f"Точное значение {function_name}: {exact_value}")
        self.vivod_isledovania.appendPlainText("\nКоэффициенты разложения в ряд Тейлора:")
        for i, coeff in enumerate(coefficients):
            self.vivod_isledovania.appendHtml(f"a<sub>{i}</sub> = {coeff}")
        error = abs(approximation - exact_value)
        self.vivod_isledovania.appendPlainText("\nАнализ точности разложения:")
        self.vivod_isledovania.appendPlainText(f"Погрешность: {error}")

    def display_convergence(self, results):
        self.vivod_isledovania.appendPlainText("\nАнализ сходимости рядов:")
        self.vivod_isledovania.appendPlainText("\nПо необходимому признаку:")
        for result in results:
            approximation, exact_value = result
            error = abs(approximation - exact_value)
            if error < 0.001:
                self.vivod_isledovania.appendPlainText("Ряд сходится.")
            else:
                self.vivod_isledovania.appendPlainText("Ряд расходится.")

            # Проверка по признаку Даламбера
            dalamber_condition = self.check_dalamber_condition(result)
            self.vivod_isledovania.appendPlainText("\nПо достаточным признакам:")
            if dalamber_condition:
                self.vivod_isledovania.appendPlainText("Признак Даламбера: Ряд сходится.")
            else:
                self.vivod_isledovania.appendPlainText("Признак Даламбера: Ряд расходится.")

            # Проверка по радикальному признаку Коши
            radical_cauchy_condition = self.check_radical_cauchy_condition(result)
            if radical_cauchy_condition:
                self.vivod_isledovania.appendPlainText("Радикальный признак Коши: Ряд сходится.")
            else:
                self.vivod_isledovania.appendPlainText("Радикальный признак Коши: Ряд расходится.")

            # Проверка по интегральному признаку Коши
            integral_cauchy_condition = self.check_integral_cauchy_condition(result)
            if integral_cauchy_condition:
                self.vivod_isledovania.appendPlainText("Интегральный признак Коши: Ряд сходится.")
            else:
                self.vivod_isledovania.appendPlainText("Интегральный признак Коши: Ряд расходится.")

            self.vivod_isledovania.appendPlainText("_____________________________________________")

    def check_dalamber_condition(self, coefficients):
        limit = abs(coefficients[-1] / coefficients[-2])
        return limit < 1

    def check_radical_cauchy_condition(self, coefficients):
        limit = (abs(coefficients[-1])) ** (1 / len(coefficients))
        return limit < 1

    def check_integral_cauchy_condition(self, coefficients):
        remainder_sum = sum(coefficients)
        return remainder_sum < 1

    def plot_graphs(self):
        try:
            xlim_sinx = (-6.3, 6.3)
            ylim_sinx = (-1.2, 1.2)

            xlim_cosx = (-6.3, 6.3)
            ylim_cosx = (-1.2, 1.2)

            xlim_tgx = (-8, 8)
            ylim_tgx = (-20, 20)

            xlim_ctgx = (-8, 8)
            ylim_ctgx = (-20, 20)

            if self.func_sinx.isChecked():
                self.show_sinx_graph(xlim_sinx, ylim_sinx)
            if self.func_cosx.isChecked():
                self.show_cosx_graph(xlim_cosx, ylim_cosx)
            if self.func_tgx.isChecked():
                self.show_tgx_graph(xlim_tgx, ylim_tgx)
            if self.func_ctgx.isChecked():
                self.show_ctgx_graph(xlim_ctgx, ylim_ctgx)
        except Exception as e:
            print("An error occurred:", e)

    def show_sinx_graph(self, xlim, ylim):
        x_values = np.linspace(-20 * np.pi, 20 * np.pi, 2000)
        terms = int(self.tochnost_razlojenia.currentText())
        self.plot_sinx(x_values, terms, xlim, ylim, title="График функции sin(x)")

    def show_cosx_graph(self, xlim, ylim):
        x_values = np.linspace(-20 * np.pi, 20 * np.pi, 2000)
        terms = int(self.tochnost_razlojenia.currentText())
        self.plot_cosx(x_values, terms, xlim, ylim, title="График функции cos(x)")

    def show_tgx_graph(self, xlim, ylim):
        x_values = np.linspace(-20 * np.pi, 20 * np.pi, 2000)
        terms = int(self.tochnost_razlojenia.currentText())
        self.plot_tgx(x_values, terms, xlim, ylim, title="График функции tg(x)")

    def show_ctgx_graph(self, xlim, ylim):
        x_values = np.linspace(-20 * np.pi, 20 * np.pi, 2000)
        terms = int(self.tochnost_razlojenia.currentText())
        self.plot_ctgx(x_values, terms, xlim, ylim, title="График функции ctg(x)")

    def plot_sinx(self, x_values, terms, xlim, ylim, title):
        sin_exact = np.sin(x_values)
        sin_approximation, _ = sin_taylor(x_values, terms)
        self.plot_graph(x_values, sin_exact, sin_approximation, 'Точное значение sin(x)', 'Разложение sin(x)', xlim,
                        ylim, title)

    def plot_cosx(self, x_values, terms, xlim, ylim, title):
        cos_exact = np.cos(x_values)
        cos_approximation, _ = cos_taylor(x_values, terms)
        self.plot_graph(x_values, cos_exact, cos_approximation, 'Точное значение cos(x)', 'Разложение cos(x)', xlim,
                        ylim, title)

    def plot_tgx(self, x_values, terms, xlim, ylim, title):
        tan_exact = np.tan(x_values)
        tg_approximation, _ = tg_taylor(x_values, terms)
        self.plot_graph(x_values, tan_exact, tg_approximation, 'Точное значение tg(x)', 'Разложение tg(x)', xlim, ylim, title)

    def plot_ctgx(self, x_values, terms, xlim, ylim, title):
        cot_exact = 1 / np.tan(x_values)
        ctg_approximation, _ = ctg_taylor(x_values, terms)

        # Фильтрация данных, исключение точек близких к вертикальным асимптотам
        tolerance = 1e-10  # Порог для определения близких к нулю значений
        x_filtered = x_values[np.abs(np.sin(x_values)) > tolerance]
        cot_filtered = cot_exact[np.abs(np.sin(x_values)) > tolerance]
        ctg_approx_filtered = ctg_approximation[np.abs(np.sin(x_values)) > tolerance]

        # Построение графика
        self.plot_graph(x_filtered, cot_filtered, ctg_approx_filtered, 'Точное значение ctg(x) ',
                        'Разложение ctg(x)', xlim, ylim, title)

    def plot_graph(self, x_values, exact_values, approx_values, exact_label, approx_label, xlim, ylim, title):
        fig, ax = plt.subplots(figsize=(10, 6))

        # График функций
        ax.plot(x_values, exact_values, label=exact_label, color='blue')
        ax.plot(x_values, approx_values, label=approx_label, linestyle='--', color='red')

        # Оси координат
        ax.axhline(0, color='black', linewidth=1.5)  # Ox
        ax.axvline(0, color='black', linewidth=1.5)  # Oy

        # Подписи к осям
        ax.set_xlabel('y')
        ax.set_ylabel('x', rotation=0)

        # Положение подписей осей
        ax.xaxis.set_label_position('top')
        ax.yaxis.set_label_position('right')

        # Отображение границ справа и сверху
        ax.spines['right'].set_visible(True)
        ax.spines['top'].set_visible(True)

        # Установка позиции осей координат
        ax.spines['left'].set_position('zero')
        ax.spines['bottom'].set_position('zero')
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)

        # Установка начального масштаба
        ax.set_xlim(xlim)
        ax.set_ylim(ylim)
        ax.set_title(title)
        # Легенда
        ax.legend()

        # Сетка
        ax.grid(True)
        ax.figure.canvas.mpl_connect('scroll_event', self.on_scroll)

        # Показываем график
        plt.show()

    def on_scroll(self, event):
        if event.button == 'up':
            scale_factor = 1.1
        elif event.button == 'down':
            scale_factor = 1 / 1.1
        else:
            scale_factor = 1.0

        ax = event.inaxes
        if ax is not None:
            xlim = ax.get_xlim()
            ylim = ax.get_ylim()

            x_center = np.mean(xlim)
            y_center = np.mean(ylim)

            x_new_width = (xlim[1] - xlim[0]) * scale_factor
            y_new_height = (ylim[1] - ylim[0]) * scale_factor

            ax.set_xlim([x_center - x_new_width / 2, x_center + x_new_width / 2])
            ax.set_ylim([y_center - y_new_height / 2, y_center + y_new_height / 2])

            ax.figure.canvas.draw_idle()

    def clear_output(self):
        self.vivod_isledovania.clear()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Taylor_series = QtWidgets.QMainWindow()
    ui = Ui_Taylor_series()
    ui.setupUi(Taylor_series)
    Taylor_series.show()
    sys.exit(app.exec_())

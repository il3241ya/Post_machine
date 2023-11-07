import customtkinter
from POST_MACHINE_class import post_machine
from PIL import Image


class App(customtkinter.CTk, post_machine):
    """
    class App(customtkinter.CTk, post_machine),
    наследует от customtkinter.CTk, post_machine.

    Назначение - класс приложения, для работы
    с машиной Поста. В нем реализован весь необходимый интерфейс
    и логика работы


    -------------------------------------------------------------

    Methods

    __init__()
        Выполняется всякий раз, когда из класса создаётся объект.
        Создаются все виджеты программы.

    btn_information_met(self)
        Метод создающий окно информации о проекте,
        вызывается кнопкой из бокового меню.

    btn_commands_met(self)
        Метод создающий окно с обучением,
        вызывается кнопкой из бокового меню.

    btn_post_mac_met(self)
        Метод создающий окно со справкой о машине Поста,
        вызывается кнопкой из бокового меню.

    btn_ready_com_met(self)
        Метод создающий окно с готовыми примерами команд,
        вызывается кнопкой из бокового меню.

    _fix1(self)
        Метод созданный для уменьшения ошибок ввода пользователем,
        не дающий перейти к следующему шагу, пока не сделан предыдущий.

    _fix2(self)
        Метод созданный для уменьшения ошибок ввода пользователем,
        не дающий перейти к следующему шагу, пока не сделан предыдущий.

    _corect_step(self, step1)
        Метод проверяющий корректность номера выполняемой команды.
        В программе не может быть номеров с отрицательным значением
        или номеров больших, чем колличество команд.
        -------------------------------------------------------------
        Arguments
        step1 номер выполняемой команды
        -------------------------------------------------------------
        Return
        True/False в зависимости от корректности шага

    _corect_input_tape(self, tape)
        Метод проверяющий корректность начального состояния ленты машины,
        введенного пользователем. (В ленте не может быть что-то кроме
        0 и 1 или пустоты).
        -------------------------------------------------------------
        Arguments
        tape начальное состояние ленты
        -------------------------------------------------------------
        Return
        возвращает True/False в зависимости от корректности ленты

    _reset(self)
        Метод сбрасывающий весь контент виджетов, при нажатии на кнопку
        Нужен для подчистки памяти.

    _start(self)
        Метод описывающий работу машины и соединяющий возвращаемые значения,
        из класса post_machine(), и интерфейс программы. Запускается при
        нажатии на кнопку "начать выполнение" в интерфейсе. Результатом
        работы данного метода является моделирование машины Поста
        выполняющую программу пользователя.
    """

    def __init__(self):
        """
        Выполняется всякий раз, когда из класса создаётся объект.
        Создаются все виджеты программы.
        """
        super().__init__()  # Функция super() позволяет наследовать базовые классы без необходимости явно ссылаться на базовый класс

        # инициализируем окно программы, задаем его размер, название, цветовую тему, и сетку размещения элементов
        self.title("Post machine simulator")
        self.geometry("1200x1000")
        self.minsize(1200, 1000)
        self.maxsize(1200, 1000)

        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("green")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # окно разбито на три части
        # инициализируем первую часть(боковое меню). Создаем и размещаем все элементы в нем

        #############################################
        # фрейм один(меню)
        #############################################

        # создаём базовый фрейм и размещаем его в общем окне

        self.frame_menu = customtkinter.CTkFrame(self)
        self.frame_menu.grid(column=0, row=0, rowspan=4, padx=(15, 0), pady=15, sticky="NSEW")

        # создаем и размещаем логотип/название приложения

        self.label_logo = customtkinter.CTkLabel(self.frame_menu, text="_Post \nmachine", font=("Segoe UI", 64),
                                                 compound="center", anchor="center")
        self.label_logo.grid(column=0, row=0, padx=20, pady=(20, 50), sticky="ew")

        # создаем первую кнопку, с информацией о проекте

        self.btn_information = customtkinter.CTkButton(self.frame_menu, text="СПРАВКА О ПРОЕКТЕ", width=200, height=32,
                                                       font=("Segoe UI", 22), fg_color="#353535", text_color="#888888",
                                                       command=self.btn_information_met)
        self.btn_information.grid(column=0, row=2, padx=20, pady=(10, 10), sticky="ew")

        # создаем вторую кнопку, с обучением и списком команд

        self.btn_commands = customtkinter.CTkButton(self.frame_menu, text="ОБУЧЕНИЕ", width=200, height=32,
                                                    font=("Segoe UI", 22), fg_color="#353535", text_color="#888888",
                                                    command=self.btn_commands_met)
        self.btn_commands.grid(column=0, row=3, padx=20, pady=(0, 10), sticky="ew")

        # создаем третью кнопку, со справкой о машине Поста

        self.btn_post_mac = customtkinter.CTkButton(self.frame_menu, text="МАШИНА ПОСТА", width=200, height=32,
                                                    font=("Segoe UI", 22), fg_color="#353535", text_color="#888888",
                                                    command=self.btn_post_mac_met)
        self.btn_post_mac.grid(column=0, row=4, padx=20, pady=(0, 10), sticky="ew")

        # создаем четвертую кнопку, с примерами готовых команд

        self.btn_ready_command = customtkinter.CTkButton(self.frame_menu, text="ГОТОВЫЕ КОМАНДЫ", width=200, height=32,
                                                         font=("Segoe UI", 22), fg_color="#353535",
                                                         text_color="#888888", command=self.btn_ready_com_met)
        self.btn_ready_command.grid(column=0, row=5, padx=20, pady=(0, 10), sticky="s")

        # создаем пятую кнопку, очистки окна

        self.btn_reset_command = customtkinter.CTkButton(self.frame_menu, text="ОЧИСТИТЬ ВИДЖЕТЫ", width=200, height=32,
                                                         font=("Segoe UI", 22), fg_color="#353535",
                                                         text_color="#888888", command=self._reset)
        self.btn_reset_command.grid(column=0, row=6, padx=20, pady=(0, 10), sticky="s")

        #############################################
        #############################################

        #############################################
        # фрейм два(реализованы виджеты ввода)
        #############################################

        # создаем второй фрейм на котором будут находиться все функции ввода.

        self.frame_inputConsole = customtkinter.CTkFrame(self, height=350)
        self.frame_inputConsole.grid(column=1, row=0, rowspan=1, padx=15, pady=(15, 0), sticky="NSEW")

        # заголовок Ввод программы

        self.headline_command_input_field = customtkinter.CTkTextbox(self.frame_inputConsole, width=50, height=20,
                                                                     font=("Segoe UI", 32), activate_scrollbars=False,
                                                                     fg_color="#2B2B2B")
        self.headline_command_input_field.grid(row=0, column=0, padx=15, pady=(15, 0), sticky="NSEW")
        self.headline_command_input_field.insert("0.0", "Ввод программы")
        self.headline_command_input_field.configure(state="disabled")

        # поле ввода программы

        self.command_input_field = customtkinter.CTkTextbox(self.frame_inputConsole, width=300, height=305,
                                                            font=("Segoe UI", 32), activate_scrollbars=True,
                                                            fg_color="#2f2f2f")
        self.command_input_field.grid(row=1, rowspan=3, column=0, padx=15, pady=(0, 20), sticky="NSEW")
        self.command_input_field.configure(state="disabled")

        # заголовок Ввод начального состояния ленты

        self.headline_first_tape_input_field = customtkinter.CTkTextbox(self.frame_inputConsole, width=50, height=20,
                                                                        font=("Segoe UI", 32),
                                                                        activate_scrollbars=False, fg_color="#2B2B2B")
        self.headline_first_tape_input_field.grid(row=0, column=1, padx=15, pady=(15, 0), sticky="NSEW")
        self.headline_first_tape_input_field.insert("0.0", "Ввод начального состояния ленты")
        self.headline_first_tape_input_field.configure(state="disabled")

        # поле ввода начального состояния ленты

        self.first_tape_input_field = customtkinter.CTkTextbox(self.frame_inputConsole, width=550, height=100,
                                                               font=("Segoe UI", 32), activate_scrollbars=True,
                                                               fg_color="#2f2f2f")
        self.first_tape_input_field.grid(row=1, rowspan=2, column=1, padx=15, sticky="n")

        # чекбокс для ввода начального состояния ленты, не нажав на него, вы не сможите перейти к заполнению остальной программы

        self.check_first_tape_input_field = customtkinter.CTkCheckBox(master=self.frame_inputConsole,
                                                                      text="Зафиксировать начальное состояние ленты",
                                                                      onvalue=1, offvalue=0, command=self._fix1, font=("Segoe UI", 32))
        self.check_first_tape_input_field.grid(row=2, column=1, padx=15, pady=55, sticky="nw")

        # чекбокс для ввода программы, не нажав на него, вы не сможете перейти к выполнению программы

        self.check_command_input_field = customtkinter.CTkCheckBox(master=self.frame_inputConsole,
                                                                   text="Зафиксировать программу", onvalue=1,
                                                                   offvalue=0, command=self._fix2, font=("Segoe UI", 32))
        self.check_command_input_field.grid(row=4, column=0, padx=15, pady=(0, 20), sticky="nw")
        self.check_command_input_field.configure(state='disabled')

        # кнопка начала выполнения программы

        self.btn_start = customtkinter.CTkButton(self.frame_inputConsole, text="Начать выполнение", width=300,
                                                 height=32, font=("Segoe UI", 22), fg_color="#2FA572",
                                                 text_color="#2B2B2B", command=self._start)
        self.btn_start.grid(column=0, row=5, padx=15, pady=(0, 20), sticky="nw")
        self.btn_start.configure(state="disabled")

        #############################################
        #############################################

        #############################################
        # фрейм три(реализованы виджеты вывода)
        #############################################

        # создаем и размещаем на нем все элементы вывода на 3 фрейме

        self.frame_outputConsole = customtkinter.CTkFrame(self, border_width=2, border_color='#2FA572')

        self.frame_outputConsole.grid(column=1, row=1, rowspan=2, padx=15, pady=15, sticky="n")

        # заголовок Лента машины

        self.headline_tape = customtkinter.CTkTextbox(self.frame_outputConsole, width=50, height=20,
                                                      font=("Segoe UI", 32), activate_scrollbars=False,
                                                      fg_color="#2B2B2B")
        self.headline_tape.grid(row=0, column=0, padx=15, pady=(15, 0), sticky="NSEW")
        self.headline_tape.insert("0.0", "Лента машины")
        self.headline_tape.configure(state="disabled")

        # окно вывода ленты

        self.output = customtkinter.CTkTextbox(self.frame_outputConsole, height=50, width=800, font=("Segoe UI", 32),
                                               activate_scrollbars=False)
        self.output.grid(row=1, column=0, padx=0, pady=(5, 5), sticky="n")
        self.output.configure(state="normal")
        self.output.insert("0.0",
                           '0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0')
        self.output.configure(state="disabled")

        # пишущая головка машины

        self.write_head_line = customtkinter.CTkSlider(self.frame_outputConsole, width=800, progress_color="#4A4D50")
        self.write_head_line.grid(row=2, column=0, padx=20)
        self.write_head_line.configure(state="disabled")

        # заголовок Команда (показывает на какой команде завершилось выполнение)

        self.headline_step = customtkinter.CTkTextbox(self.frame_outputConsole, width=50, height=20,
                                                      font=("Segoe UI", 32), activate_scrollbars=False,
                                                      fg_color="#2B2B2B")
        self.headline_step.grid(row=3, column=0, padx=15, pady=(15, 0), sticky="NSEW")
        self.headline_step.insert("0.0", "Команда")
        self.headline_step.configure(state="disabled")

        # вывод последней команды (показывает на какой команде завершилось выполнение)

        self.step_out = customtkinter.CTkTextbox(self.frame_outputConsole, width=300, height=40,
                                                 font=("Segoe UI", 32),
                                                 activate_scrollbars=False)
        self.step_out.grid(row=4, padx=20, sticky="w")
        self.step_out.configure(state="disabled")

        # заголовок Результат выполнения

        self.headline_comp = customtkinter.CTkTextbox(self.frame_outputConsole, width=50, height=20,
                                                      font=("Segoe UI", 32), activate_scrollbars=False,
                                                      fg_color="#2B2B2B")
        self.headline_comp.grid(row=5, column=0, padx=15, pady=(15, 0), sticky="NSEW")
        self.headline_comp.insert("0.0", "Результат выполнения")
        self.headline_comp.configure(state="disabled")

        # виджет результата выполнения

        self.rezult = customtkinter.CTkTextbox(self.frame_outputConsole, width=300, height=140, font=("Segoe UI", 32),
                                               activate_scrollbars=True)
        self.rezult.grid(row=6, column=0, pady=(0, 20), padx=20, sticky="NSEW")
        self.rezult.configure(state="disabled")

        #############################################
        #############################################

    def btn_information_met(self):
        """
        Метод создающий окно информации о проекте,
        вызывается кнопкой из бокового меню
        """

        # window_information - всплывающее окно
        window_information = customtkinter.CTkToplevel(self)
        window_information.title("PMS cправка о проекте")
        window_information.geometry("700x250")
        window_information.maxsize(700, 250)

        # inf_text - текстовое окно
        inf_text = customtkinter.CTkTextbox(window_information, width=400, height=250,
                                            font=("Segoe UI", 32), activate_scrollbars=False,
                                            fg_color="#242424")
        inf_text.pack(side="top", fill="both", expand=True, pady=10, padx=10)

        inf_text.insert("0.0", "-----------------------------------------------------------------------------------\n"
                               "Автор: Долгов Илья БИБ223\n"
                               "-----------------------------------------------------------------------------------\n"
                               "Название: Моделирование машины Поста с примерами алгоритмов\n"
                               "-----------------------------------------------------------------------------------\n"
                               "Github: https://github.com/Caaaaactus/Post-Machine.git\n"
                               "-----------------------------------------------------------------------------------\n")
        inf_text.configure(state="disabled")

    def btn_commands_met(self):
        """
        Метод создающий окно с обучением,
        вызывается кнопкой из бокового меню
        """
        # Создаем высплывающее окно
        window_commands = customtkinter.CTkToplevel(self)
        window_commands.title("PMS обучение")
        window_commands.geometry("950x500")
        window_commands.maxsize(950, 500)

        # Создаем текстовое поле
        edu_text = customtkinter.CTkTextbox(window_commands, width=400, height=250,
                                            font=("Segoe UI", 32), activate_scrollbars=False,
                                            fg_color="#242424")
        edu_text.pack(side="top", fill="both", expand=True, pady=10, padx=10)

        edu_text.insert("0.0",
                        "------------------------------------------------------------------------------------------------------------------\n"
                        "------------------------------------------------------------------------------------------------------------------\n"
                        "                                                                               Команды                            \n"
                        "------------------------------------------------------------------------------------------------------------------\n"
                        " v     | Поставить метку в ячейку\n"
                        "------------------------------------------------------------------------------------------------------------------\n"
                        " -     | Убрать метку в ячейку\n"
                        "------------------------------------------------------------------------------------------------------------------\n"
                        " >    | Передвинуть головку машины вправо\n"
                        "------------------------------------------------------------------------------------------------------------------\n"
                        " <    | Передвинуть головку машины влево\n"
                        "------------------------------------------------------------------------------------------------------------------\n"
                        " ?i,j  | В случае если метка в ячейке стоит, то перейти к команде j, если метки нет, то к команде i\n"
                        "------------------------------------------------------------------------------------------------------------------\n"
                        " s     | Поставить метку в ячейку\n"
                        "------------------------------------------------------------------------------------------------------------------\n"
                        "------------------------------------------------------------------------------------------------------------------\n"
                        "                                                                                                                  \n"
                        "                                                                                                                  \n"
                        "------------------------------------------------------------------------------------------------------------------\n"
                        "------------------------------------------------------------------------------------------------------------------\n"
                        "                                                                      Пример программы                            \n"
                        "------------------------------------------------------------------------------------------------------------------\n"
                        "v2\n"
                        "?1,3\n"
                        ">4\n"
                        "?5,3\n"
                        "s5\n"
                        "------------------------------------------------------------------------------------------------------------------\n"
                        "*Все команды необоходимо писать без пробелов, а саму программу без пустых строк.\n Больше примеров программ можете найти в соответствующей вкладке\n"
                        "------------------------------------------------------------------------------------------------------------------\n"
                        "------------------------------------------------------------------------------------------------------------------\n"
                        "                                                                                                                  \n"
                        "                                                                                                                  \n"
                        "------------------------------------------------------------------------------------------------------------------\n"
                        "------------------------------------------------------------------------------------------------------------------\n"
                        "                                                                  Результаты выполнения                           \n"
                        "------------------------------------------------------------------------------------------------------------------\n"
                        "Программа не может окончить свое выполнение в связи с ошибкой\n"
                        "------------------------------------------------------------------------------------------------------------------\n"
                        "- Перепроверьте свою программу на ошибки постановки метки в занятую ячейку \nили попытке убрать метку из пустой ячейки\n"
                        "------------------------------------------------------------------------------------------------------------------\n"
                        "Программа зациклилась и превысила допустимое колличество шагов. Перепишите программу \nтак, чтобы она выполнялась не боллее чем за 300 шагов\n"
                        "------------------------------------------------------------------------------------------------------------------\n"
                        "- Перепроверьте свою программу на ошибки зацикливания, часто такое происходит\n"
                        "  при использовании ветвлений (?i,j) ИЛИ ЕСЛИ ВЫ ВЫПОЛНЯЕТЕ ПРОГРАММУ ДЛЯ ВЫЧИТАНИЯ\n"
                        "------------------------------------------------------------------------------------------------------------------\n"
                        "Программа окончила свое выполнение без ошибок\n"
                        "------------------------------------------------------------------------------------------------------------------\n"
                        "- Программа не имеет ошибок или зацикливаний\n"
                        "------------------------------------------------------------------------------------------------------------------\n"
                        "------------------------------------------------------------------------------------------------------------------\n"
                        "                                                                                                                  \n"
                        "                                                                                                                  \n"
                        "------------------------------------------------------------------------------------------------------------------\n"
                        "------------------------------------------------------------------------------------------------------------------\n"
                        "                                                               Алгоритм работы программы                          \n"
                        "------------------------------------------------------------------------------------------------------------------\n"
                        "1. Введите начальное состояние ленты, 0 - пустая ячейка, 1 - ячейка с меткой.\n"
                        "   Если вам нужна просто пустая лента, то можете оставить это окно пустым.\n"
                        "   После чего необходимо поставить галочку в чекбокс\n"
                        "   'Зафиксировать начальное состояние ленты'\n"
                        "   *Обратите внимание на то, что индекс пишущей головки считается по формуле\n"
                        "   I = (60 + длинна введенного участка ленты)//2\n"
                        "------------------------------------------------------------------------------------------------------------------\n"
                        "2. После того как вы ввели начальную ленту и ОБЯЗАТЕЛЬНО нажали на чекбокс\n "
                        "   'Зафиксировать начальное состояние ленты'\n"
                        "   Вам необходиом ввести саму программу для машины Поста\n"
                        "   С правилами ввода программы ознакомьтесь выше\n"
                        "   После чего необходимо поставить галочку в чекбокс 'Зафиксировать программу'\n"
                        "------------------------------------------------------------------------------------------------------------------\n"
                        "3. После того как вы ввели программу и ОБЯЗАТЕЛЬНО нажали на чекбокс\n"
                        "   'Зафиксировать программу'\n"
                        "   Необходимо нажать на кнопку 'Начать выполнение'\n"
                        "------------------------------------------------------------------------------------------------------------------\n"
                        "4. Если вы все выполнели по данной инструкции, то внизу вам будет выведен результат\n"
                        "   выполнения программы, лента, а так же шаг\n"
                        "   на котором закончила выполнение программа\n"
                        "   С возможными резуультатами вывода и их значением, можете ознакомиться выше\n"
                        "------------------------------------------------------------------------------------------------------------------\n"
                        "5. ОБЯЗАТЕЛЬНО ПОСЛЕ КАЖДОГО ВЫПОЛНЕНИЯ НАЖИМАЙТЕ КНОПКУ 'ОЧИСТИТЬ ВИДЖЕТЫ'\n"
                        "   выполнения программы, лента, а так же шаг\n"
                        "   на котором закончила выполнение программа\n"
                        "   С возможными резуультатами вывода и их значением, можете ознакомиться выше\n"
                        "------------------------------------------------------------------------------------------------------------------\n"
                        "------------------------------------------------------------------------------------------------------------------\n")
        edu_text.configure(state="disabled")

    def btn_post_mac_met(self):
        """
        Метод создающий окно со справкой о машине Поста,
        вызывается кнопкой из бокового меню
        """

        # Создаем высплывающее окно
        window_post_mac = customtkinter.CTkToplevel(self)
        window_post_mac.geometry("900x500")
        window_post_mac.title("PMS информация о машине Поста")
        text = customtkinter.CTkTextbox(window_post_mac,
                                        font=("Segoe UI", 32),
                                        activate_scrollbars=False,
                                        fg_color="#242424")
        # Создаем текстовое поле
        text.pack(side="top", fill="both", expand=True, padx=20, pady=10)
        text.configure(state="normal")
        text.insert("0.0", "Маши́на По́ста — абстрактная вычислительная машина, \n"
                           "предложенная Эмилем Постом в 1936 году, создана независимо от машины \n"
                           "Тьюринга, но сообщение о машине Поста опубликовано на несколько месяцев \n"
                           "позднее. Отличается от машины Тьюринга большей простотой, притом обе \n"
                           "машины алгоритмически «эквивалентны» и обе разработаны для формализации \n"
                           "понятия алгоритма и решения задач об алгоритмической разрешимости, то есть, \n"
                           "демонстрации алгоритмического решения задач в форме последовательности команд \n"
                           "для машины Поста.")
        text.configure(state="disabled")
        # Переменная для храния изображения ленты
        img_tape = customtkinter.CTkImage(light_image=Image.open("img/tape.png"),
                                          dark_image=Image.open("img/tape.png"),
                                          size=(850, 150))
        # добавление изображения в window_post_mac
        label_img = customtkinter.CTkLabel(window_post_mac, image=img_tape, text="")
        label_img.pack(side="bottom", fill="both", expand=True, padx=20, pady=20)

    def btn_ready_com_met(self):
        """
        Метод создающий окно с готовыми примерами команд,
        вызывается кнопкой из бокового меню
        """

        # Создаем высплывающее окно
        window_programs = customtkinter.CTkToplevel(self)
        window_programs.title("PMS  готовые команды")
        window_programs.geometry("950x500")
        window_programs.maxsize(950, 500)

        # Создаем текстовое поле
        ready_command_text = customtkinter.CTkTextbox(window_programs, width=400, height=250,
                                                      font=("Segoe UI", 32), activate_scrollbars=False,
                                                      fg_color="#242424")
        ready_command_text.pack(side="top", fill="both", expand=True, pady=10, padx=10)

        ready_command_text.insert("0.0",
                                  "------------------------------------------------------------------------------------------------------------------\n"
                                  "------------------------------------------------------------------------------------------------------------------\n"
                                  "                                                                      Примеры программ                            \n"
                                  "------------------------------------------------------------------------------------------------------------------\n"
                                  "Программа прибавления к числу 1\n"
                                  "Начальное состояние ленты 1111\n"
                                  "?2,3\n"
                                  "v4\n"
                                  ">1\n"
                                  "s4\n"
                                  "------------------------------------------------------------------------------------------------------------------\n"
                                  "Программа вычитания из числа 1\n"
                                  "Начальное состояние ленты 1111111111\n"
                                  "?2,3\n"
                                  "<4\n"
                                  ">1\n"
                                  "-5\n"
                                  "s5\n"
                                  "------------------------------------------------------------------------------------------------------------------\n"
                                  "Сложение двух чисел\n"
                                  "Начальное состояние ленты 111100011\n"
                                  "?2,3\n"
                                  ">1\n"
                                  "?4,5\n"
                                  "<6\n"
                                  ">3\n"
                                  "-7\n"
                                  "<8\n"
                                  "?9,10\n"
                                  "?11,12\n"
                                  "<8\n"
                                  "<9\n"
                                  ">13\n"
                                  "v14\n"
                                  ">1\n"
                                  "------------------------------------------------------------------------------------------------------------------\n"
                                  "Разность двух чисел\n"
                                  "Начальное состояние ленты 1110011\n"
                                  "?2,3\n"
                                  ">1\n"
                                  "?4,5\n"
                                  "<6\n"
                                  ">3\n"
                                  "-7\n"
                                  "<8\n"
                                  "?9,10\n"
                                  "?11,12\n"
                                  "<8\n"
                                  "<9\n"
                                  "-13\n"
                                  ">1\n"
                                  "------------------------------------------------------------------------------------------------------------------\n"
                                  "------------------------------------------------------------------------------------------------------------------\n")
        ready_command_text.configure(state="disabled")

    def _fix1(self):
        """
        Метод созданный для уменьшения ошибок ввода пользователем,
        не дающий перейти к следующему шагу, пока не сделан предыдущий
        """
        if not self.check_first_tape_input_field.get():  # действия выполняемые в случае, если чек бокс не был активен
            self.first_tape_input_field.configure(state="normal")
            self.command_input_field.configure(state="disabled")
            self.check_command_input_field.configure(state='disabled')

        else:  # действия выполняемые в случае, если чек бокс активен
            self.first_tape_input_field.configure(state="disabled")
            self.command_input_field.configure(state="normal")
            self.check_command_input_field.configure(state='normal')

    def _fix2(self):
        """
        Метод созданный для уменьшения ошибок ввода пользователем,
        не дающий перейти к следующему шагу, пока не сделан предыдущий
        """
        if self.check_command_input_field.get():  # действия выполняемые в случае, если чек бокс был активен
            self.command_input_field.configure(state="disabled")
            self.btn_start.configure(state="normal")
        else:  # действия выполняемые в случае, если чек не бокс был активен
            self.command_input_field.configure(state="normal")
            self.btn_start.configure(state="disabled")

    def _corect_step(self, step1):
        """
        Метод проверяющий корректность номера выполняемой команды. В программе не может быть
        номеров с отрицательным значением или номеров больших,
        чем количество команд, или шагов в виде символов

        ----------------------------------------------------------------

        Arguments
        step1 номер выполняемой команды

        ----------------------------------------------------------------

        Return
        True/False в зависимости от корректности шага
        """
        if type(step1) != int:
            return False
        elif int(step1) <= 0:
            return False
        elif int(step1) > len(self.command_list):
            return False
        else:
            return True

    def _corect_input_tape(self, tape):
        """
        Метод проверяющий корректность начального состояния ленты машины, введенного
        пользователем. (В ленте не может быть что-то кроме 0 и 1 или пустоты)

        ----------------------------------------------------------------

        Arguments
        tape начальное состояние ленты

        ----------------------------------------------------------------

        Return
        возвращает True/False в зависимости от корректности ленты
        """
        for i in tape:
            if i not in '01':
                return False
        return True

    def _reset(self):
        """
        Метод сбрасывающий весь контент виджетов, при нажатии на кнопку
        Нужен для подчистки памяти
        """
        self.output.configure(state="normal")
        self.output.delete('0.0', 'end')
        self.output.edit_reset()
        self.output.configure(state="disabled")

        self.step_out.configure(state="normal")
        self.step_out.delete('0.0', 'end')
        self.step_out.edit_reset()
        self.step_out.configure(state="disabled")

        self.rezult.configure(state="normal")
        self.rezult.delete('0.0', 'end')
        self.rezult.edit_reset()
        self.rezult.configure(state="disabled")

        self.command_input_field.configure(state="normal")
        self.command_input_field.configure()
        self.command_input_field.delete('0.0', "end")
        self.command_input_field.edit_reset()
        self.command_input_field.configure(state="disabled")

        self.first_tape_input_field.configure(state="normal")
        self.first_tape_input_field.delete('0.0', 'end')
        self.first_tape_input_field.edit_reset()
        self.first_tape_input_field.configure(state="disabled")

        if self.check_command_input_field.get()==1:
            self.check_command_input_field.toggle()
        if  self.check_first_tape_input_field.get()==1:
            self.check_first_tape_input_field.toggle()

        self.output.configure(state="normal")
        self.output.insert("0.0",
                           '0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0')
        self.output.configure(state="disabled")

    def _start(self):
        """
        Метод описывающий работу машины и соединяющий возвращаемые значения, из класса
        post_machine(), и интерфейс программы. Запускается при нажатии на кнопку
        "начать выполнение" в интерфейсе. Результатом работы данного метода является
        моделирование машины Поста выполняющую программу пользователя
        """

        # считываем список команд
        self.command_list = []  # список в котором хранятся все команды программы

        self.line_commands_str = self.command_input_field.get('0.0', 'end').split(
            '\n')  # переменная необходимая чтобы считать все команды из окна ввода програмыы и добавить их в self.comamnd_list

        self.command_list += self.line_commands_str

        # Убираем пробелы
        for i in range(len(self.command_list)):
            self.command_list[i] = self.command_list[i].replace(' ', '')
        self.command_list = self.command_list[:-1]

        # считываем изначальное состояние ленты
        self.first_tape_list = []  # список для начального состояние ленты, вводимое пользователем

        line_first_tape_str = self.first_tape_input_field.get('0.0', 'end').split(
            '\n')  # строковая переменная необходимая, чтобы считать начальное состояние ленты и занести его в self.first_tape_list
        line_first_tape_str = line_first_tape_str[:-1]
        for i in line_first_tape_str[0]:
            self.first_tape_list.append(i)
        self.first_tape_list += ['0'] * 30
        self.first_tape_list[:0] = ['0'] * 30

        # присваиваем индекс пишущей головки машины
        self.wr_head = len(
            self.first_tape_list) // 2  # индекс пишущей головки машины, вначале задаем ей положение в середине

        # инициализируем машину
        p_m = post_machine(True, self.first_tape_list, self.wr_head)  # создаем объект из класса post_machine()

        # делаем запуск
        work = True  # состояние машины
        step = 1  # номер выполняемой команды
        iter = 0  # шаг
        maxIter = 300  # максимальное кол-во шагов
        current_tape = []  # текущее состояние ленты

        # В первую очередь проверяем корректность ленты
        if self._corect_input_tape(self.first_tape_list):
            # пока состоянием машины True и программа не превысила максимальное количество шагов
            while work and iter <= maxIter:
                # проверяем корректность номера шага
                if self._corect_step(step):

                    current_command = self.command_list[step - 1][0]  # текущая команда

                    self.step_out.configure(state="normal")
                    self.step_out.delete("0.0", "end")
                    self.step_out.insert("0.0", self.command_list[step - 1])
                    self.step_out.insert("0.1", ': ')
                    self.step_out.insert("0.2", step)
                    self.step_out.configure(state="disabled")

                    ex = []  # список для хранения возвращаемых значений из метода command_method класса post_machine
                    ex = p_m.command_method(current_command)

                    # В зависимости от возвращаемых значений проигрываем один из возможных сценариев
                    if ex != "Программа не может окончить свое выполнение в связи с ошибкой" and ex != "Программа окончила свое выполнение без ошибок" and ex != 11 and ex != 22:
                        current_tape, self.wr_head = ex[0], ex[1]

                        self.output.configure(state="normal")
                        self.output.delete("0.0", "end")
                        self.output.insert("0.0", current_tape[self.wr_head - 24:self.wr_head + 25])
                        self.output.configure(state="disabled")

                        step = int(self.command_list[step - 1][1:])  # номер шага

                    elif ex == 11 or ex == 22:
                        if ex == 11:
                            step = int(self.command_list[step - 1][
                                       self.command_list[step - 1].index('?') + 1:self.command_list[step - 1].index(
                                           ',')])

                        elif ex == 22:
                            step = int(self.command_list[step - 1][self.command_list[step - 1].index(',') + 1:])

                    elif ex == "Программа не может окончить свое выполнение в связи с ошибкой":
                        self.rezult.configure(state="normal")
                        self.rezult.insert("0.0",
                                           "-------------------------------------------------------------------------------------------------\n"
                                           "Программа не может окончить свое выполнение в связи с ошибкой\n"
                                           "-------------------------------------------------------------------------------------------------\n")
                        self.rezult.configure(state="disabled")

                        self.output.delete('1.0', "END")
                        self.output.edit_reset()

                        work = False


                    elif ex == "Программа окончила свое выполнение без ошибок":
                        self.rezult.configure(state="normal")
                        self.rezult.insert("0.0",
                                           "-------------------------------------------------------------------------------------------------\n"
                                           "Программа окончила свое выполнение без ошибок\n"
                                           "-------------------------------------------------------------------------------------------------\n")
                        self.rezult.configure(state="disabled")

                        self.output.delete('1.0', "END")
                        self.output.edit_reset()

                        work = False

                    iter += 1
                else:
                    self.rezult.configure(state="normal")
                    self.rezult.insert("0.0",
                                       "-------------------------------------------------------------------------------------------------\n"
                                       "Программа ссылается на несуществующую команду\n"
                                       "-------------------------------------------------------------------------------------------------\n")
                    self.rezult.configure(state="disabled")

                    self.output.delete('1.0', "END")
                    self.output.edit_reset()

                    work = False

                if iter > maxIter:
                    self.output.configure(state="normal")
                    self.output.delete("0.0", "end")
                    if self.wr_head >= len(current_tape) // 2:
                        self.output.insert("0.0",
                                           current_tape[0:49])
                    else:
                        self.output.insert("0.0", current_tape[0:49])

                    self.output.configure(state="disabled")

                    self.rezult.configure(state="normal")
                    self.rezult.insert("0.0",
                                       "-------------------------------------------------------------------------------------------------\n"
                                       "Программа зациклилась и превысила допустимое колличество шагов. Перепишите программу так, чтобы она выполнялась не боллее чем за 300 шагов\n"
                                       "Либо вы складывали/вычитали числа\n"
                                       "-------------------------------------------------------------------------------------------------\n")
                    self.rezult.configure(state="disabled")
                    work = False
        else:
            self.rezult.configure(state="normal")
            self.rezult.insert("0.0",
                               "-------------------------------------------------------------------------------------------------\n"
                               "Некоректный ввод начального состояния ленты\n"
                               "-------------------------------------------------------------------------------------------------\n")
            self.rezult.configure(state="disabled")
            work = False

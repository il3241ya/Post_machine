class post_machine():
    """
    class post_machine()
    Назначение - моделирование работы машины
    посредством обработки текущей команды, возврат обновленной
    ленты и ошибки в случае невозможности выполнения программы

    -------------------------------------------------------------
    Methods
    get_state(self)
        Метод возвращающий состояние машины
        -------------------------------------------------------------
        Return
        self.state

    get_tape_list(self)
        Метод возвращающий ленту машины
        -------------------------------------------------------------
        Return
        self.tape_list

    get_write_head(self)
        Метод возвращающий индекс пишущей головки машины
        -------------------------------------------------------------
        Return
        self.write_head

    _can_do_command(self, current_command)
        Метод определяющий возможность выполнения той или иной команды
        поступившей машине
        -------------------------------------------------------------
        Arguments
        current_command текущая команда
        -------------------------------------------------------------
        Return
        True/False

    tape_extension(self)
        Метод удлиняющий ленту в случае необходимости
        (головка машины дошла до одного из краев)
        -------------------------------------------------------------
        Return
        self.tape_list

    command_method(self, current_command)
        Основной метод класса, моделирующий выполнение команд
        -------------------------------------------------------------
        Arguments
        current_command текущая команда
        -------------------------------------------------------------
        Return
        В случае если команду можно выполнить и она не является командой
        остановки, метод вернет
        self.tape_list, self.write_head

        В случае если команду можно выполнить и она является командой
        остановки, метод вернет
        "Программа окончила свое выполнение без ошибок"

        В случае если команду нельзя выполнить, метод вернет
        "Программа не может окончить свое выполнение в связи с ошибкой"
    """

    def __init__(self, state, tape_list, write_head):
        """
        __init__(self, state, tape_list, write_head)
        Выполняется всякий раз, когда из класса создаётся объект.
        Используется для инициализации переменных класса.
        -------------------------------------------------------------
        Arguments
        state - состояние машины (True - работает. False - не работает)
        tape_list - лента машины
        write_head - индекс пишущей головки на ленте
        """

        self.state = state
        self.tape_list = tape_list
        self.write_head = write_head

    def get_state(self):
        """
        Метод возвращающий состояние машины
        -------------------------------------------------------------
        Return
        self.state
        """

        return self.state

    def get_tape_list(self):
        """
        Метод возвращающий ленту машины
        -------------------------------------------------------------
        Return
        self.tape_list
        """

        return self.tape_list

    def get_write_head(self):
        """
        Метод возвращающий индекс пишущей головки машины
        -------------------------------------------------------------
        Return
        self.write_head
        """

        return self.write_head

    def _can_do_command(self, current_command):
        """
        Метод определяющий возможность выполнения той или иной команды
        поступившей машине
        -------------------------------------------------------------
        Arguments
        current_command текущая команда
        -------------------------------------------------------------
        Return
        True/False
        """

        #проверяем возможность выполнения команды согласно правилам работы машины
        #(невозможно поставить метку в непустое поле, как и убрать метку из пустого)
        #проверяемрй командой не может быть символ кроме v и -
        if self.tape_list[self.write_head] == '1' and current_command == 'v':
            return False
        elif self.tape_list[self.write_head] == '0' and current_command == '-':
            return False
        elif current_command != 'v' and current_command != '-':
            return False
        else:
            return True

    def tape_extension(self):
        """
        Метод удлиняющий ленту в случае необходимости
        (головка машины дошла до одного из краев)
        -------------------------------------------------------------
        Return
        self.tape_list
        """

        #расширяем ленту, если доходим до одного из ее концов
        if self.write_head == len(self.tape_list)-1:
            self.tape_list += ['0']*33
        elif self.write_head == 0:
            self.tape_list[:0] = ['0'] * 33

        return self.tape_list

    def command_method(self, current_command):
        """
        Основной метод класса, моделирующий выполнение команд
        -------------------------------------------------------------
        Arguments
        current_command текущая команда
        -------------------------------------------------------------
        Return
        В случае если команду можно выполнить и она не является командой
        остановки, метод вернет
        self.tape_list, self.write_head

        В случае если команду можно выполнить и она является командой
        остановки, метод вернет
        "Программа окончила свое выполнение без ошибок"

        В случае если команду нельзя выполнить, метод вернет
        "Программа не может окончить свое выполнение в связи с ошибкой"
        """

        #инициализируем поступившую программу и возможность ее выполнения,
        #после чего приступаем к ее реализации
        if current_command == 'v' and self._can_do_command(current_command):
            self.tape_list[self.write_head] = '1'

            return self.tape_list, self.write_head

        elif current_command == '-' and self._can_do_command(current_command):
            self.tape_list[self.write_head] = '0'

            return self.tape_list, self.write_head

        elif current_command == '>':
            if self.write_head==len(self.tape_list)-1:
                self.tape_list = self.tape_extension()
            self.write_head+=1

            return self.tape_list, self.write_head

        elif current_command == '<':
            if self.write_head == 0:
                self.tape_list = self.tape_extension()
                self.write_head=30
            else:
                self.write_head-=1

            return self.tape_list, self.write_head

        elif current_command == 's':

            return "Программа окончила свое выполнение без ошибок"

        elif current_command == '?':
            if self.tape_list[self.write_head] == '1':
                return 22
            if self.tape_list[self.write_head] == '0':
                return 11
        #в случае ошибки, возвращаем не новую ленту и индекс головки, а ошибку
        elif not self._can_do_command(current_command):

            return "Программа не может окончить свое выполнение в связи с ошибкой"


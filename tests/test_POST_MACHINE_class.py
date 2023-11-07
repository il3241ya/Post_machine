#import pytest
from POST_MACHINE_class import post_machine


def test_get_state():
    pm = post_machine(False, [0]*60, 30)
    assert pm.get_state() == False

    pm = post_machine(True, [0] * 60, 30)
    assert pm.get_state() == True

def test_get_tape_list():
    pm = post_machine(False, [0]*20, 30)
    assert pm.get_tape_list() == [0]*20

    pm = post_machine(True, "aa", 30)
    assert pm.get_tape_list() == "aa"

    pm = post_machine(True, None, 30)
    assert pm.get_tape_list() == None

def test_get_write_head():
    pm = post_machine(False, [0] * 20, 2)
    assert pm.get_write_head() == 2

    pm = post_machine(True, "aa", 1)
    assert pm.get_write_head() == 1

    pm = post_machine(True, None, 30)
    assert pm.get_write_head() == 30

def test_can_do_command():
    pm = post_machine(True, ['1']*100, 30)
    command = 'v'
    assert pm._can_do_command(command) == False

    pm = post_machine(True, ['0'] * 100, 30)
    command = 'v'
    assert pm._can_do_command(command) == True

    pm = post_machine(True, ['1'] * 100, 30)
    command = '-'
    assert pm._can_do_command(command) == True

    pm = post_machine(True, ['0'] * 100, 30)
    command = '-'
    assert pm._can_do_command(command) == False

    pm = post_machine(True, ['0'] * 100, 30)
    command = 'k'
    assert pm._can_do_command(command) == False

    pm = post_machine(True, ['0'] * 100, 30)
    command = '*'
    assert pm._can_do_command(command) == False


def test_tape_extension():
    pm = post_machine(True, ['1'] * 100, len(['1'] * 100)-1)
    assert pm.tape_extension() ==  ['1'] * 100 + ['0']*33

    pm = post_machine(True, ['0'] * 100, len(['0'] * 100) - 1)
    assert pm.tape_extension() == ['0'] * 33 + ['0'] * 100

def test_command_method():
    tape1 = ['1'] * 100
    wrh = len(tape1)//2
    pm = post_machine(True, tape1, wrh)
    command = 'v'
    assert pm.command_method(command) == "Программа не может окончить свое выполнение в связи с ошибкой"


    tape1 = ['0'] * 60
    wrh = len(tape1)//2
    pm = post_machine(True, ['0']*60, wrh)
    command = 'v'
    ex = tape1
    ex[wrh] = '1'
    assert pm.command_method(command) == (ex, wrh)


    tape1 = ['0'] * 100
    wrh = len(tape1) // 2
    pm = post_machine(True, tape1, wrh)
    command = '-'
    assert pm.command_method(command) == "Программа не может окончить свое выполнение в связи с ошибкой"


    tape1 = ['1'] * 100
    wrh = len(tape1) // 2
    pm = post_machine(True, ['1'] * 100, wrh)
    command = '-'
    ex = tape1
    ex[wrh] = '0'
    assert pm.command_method(command) == (ex, wrh)

    tape1 = ['0'] * 100
    wrh = len(tape1) // 2
    pm = post_machine(True, tape1, wrh)
    command = 's'
    assert pm.command_method(command) == "Программа окончила свое выполнение без ошибок"

    tape1 = ['0'] * 100
    wrh = len(tape1) // 2
    pm = post_machine(True, tape1, wrh)
    command = '?'
    assert pm.command_method(command) == 11

    tape1 = ['1'] * 100
    wrh = len(tape1) // 2
    pm = post_machine(True, tape1, wrh)
    command = '?'
    assert pm.command_method(command) == 22

    tape1 = ['1'] * 100
    wrh = len(tape1)-1
    pm = post_machine(True, tape1, wrh)
    command = '>'
    assert pm.command_method(command) == (['1'] * 100 + ['0']*33, wrh+1)

    tape1 = ['1'] * 100
    wrh = 0
    pm = post_machine(True, tape1, wrh)
    command = '>'
    assert pm.command_method(command) == (['1'] * 100, wrh + 1)

    tape1 = ['1'] * 100
    wrh = 0
    pm = post_machine(True, tape1, wrh)
    command = '<'
    assert pm.command_method(command) == (['0']*33 + ['1'] * 100, 30)

    tape1 = ['1'] * 100
    wrh = len(tape1)//2
    pm = post_machine(True, tape1, wrh)
    command = '<'
    assert pm.command_method(command) == (['1'] * 100, wrh-1)


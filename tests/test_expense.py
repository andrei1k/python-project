'''
This module contains unit tests for the Expense class.
'''
from datetime import datetime
from src.expense import Expense

def test_expense_creation():
    '''
    Tests the creation of an Expense object with specific attributes.
    '''
    current_time = datetime.now()
    sut = Expense(1, 'food', 'it was yummy', current_time)

    assert sut.amount == 1
    assert sut.category == 'food'
    assert sut.description == 'it was yummy'
    assert sut.date == current_time
    assert sut.currency == 'lv.'

def test_expense_to_str():
    '''
    Tests the conversion of an Expense object to a string representation.
    '''
    current_time = datetime.now()
    expense = Expense(1, 'food', 'it was yummy', current_time)

    sut = str(expense)

    assert sut == (f'Amount: 1.00 lv.\nCategory: food\nDescription: it was yummy'
                   f'\nDate: {current_time.strftime("%Y-%m-%d %H:%M:%S")}\n\n')

def test_str_to_expense():
    '''
    Tests the creation of an Expense object from a string representation.
    '''
    expense_str = '''Amount: 1.00 lv.
    Category: food
    Description: it was yummy
    Date: 2024-02-10 23:14:16'''
    sut = Expense.from_string(expense_str)

    assert sut.amount == 1
    assert sut.category == 'food'
    assert sut.description == 'it was yummy'
    assert sut.date == datetime.strptime('2024-02-10 23:14:16', '%Y-%m-%d %H:%M:%S')
    assert sut.currency == 'lv.'

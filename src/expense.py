'''
This module implements class for storing the main data for expenses in the program
'''

from datetime import datetime

class Expense:
    '''
    Represents an expense with attributes:
    - amount (float): The amount of the expense.
    - category (str): The category of the expense.
    - description (str): The description of the expense.
    - date (datetime): The date and time of the expense (default is current date and time).
    - currency (str): The currency of the expense (currently only 'lv.').
    '''
    def __init__(self, amount: float,
                 category: str, description: str,
                 date: datetime=datetime.now()) -> None:
        self.amount = amount
        self.category = category
        self.description = description
        self.date = date
        self.currency = 'lv.'

    def to_tuple(self) -> tuple[float, str, str, str, datetime]:
        '''
        Converts the Expense object to a tuple.
        :return: tuple[float, str, str, str, datetime]
        '''
        return (self.amount, self.currency, self.category, self.description, self.date)

    def __str__(self) -> str:
        '''
        Converts the Expense object to a string.
        :return: str
        '''
        return (
            f'Amount: {self.amount:.2f} {self.currency}\n'
            f'Category: {self.category}\n'
            f'Description: {self.description}\n'
            f'Date: {self.date.strftime("%Y-%m-%d %H:%M:%S")}\n\n'
        )

    @classmethod
    def from_string(cls, expense_str: str) -> 'Expense':
        '''
        Creates an Expense object from a string representation.

        :param expense_str: str
            A string representation of the Expense object.

        :return: Expense
            An Expense object created from the string representation.
        '''
        parts = expense_str.split('\n')
        amount_currency = parts[0].split(': ')[1].split(' ')
        amount = float(amount_currency[0])
        _ = amount_currency[1]
        category = parts[1].split(': ')[1]
        description = parts[2].split(': ')[1]
        date_str = parts[3].split(': ')[1]
        date = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
        return cls(amount, category, description, date)

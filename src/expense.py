"""
This module implements class for storing the main data for expenses in the program
"""

from datetime import datetime

class Expense:
    def __init__(self, amount: float,
                 category: str, description: str,
                 date: datetime=datetime.now(),currency: str='lv.') -> None:
        self.amount = amount
        self.category = category
        self.description = description
        self.date = date
        self.currency = currency

    def to_tuple(self) -> tuple[float, str, str, str, datetime]:
        return (self.amount, self.currency, self.category, self.description, self.date)

    def __str__(self) -> str:
        return (
            f'Amount: {self.amount:.2f} {self.currency}\n'
            f'Category: {self.category}\n'
            f'Description: {self.description}\n'
            f'Date: {self.date.strftime("%Y-%m-%d %H:%M:%S")}\n\n'
        )

    @classmethod
    def from_string(cls, expense_str: str) -> 'Expense':
        parts = expense_str.split('\n')
        amount_currency = parts[0].split(': ')[1].split(' ')
        amount = float(amount_currency[0])
        currency = amount_currency[1]
        category = parts[1].split(': ')[1]
        description = parts[2].split(': ')[1]
        date_str = parts[3].split(': ')[1]
        date = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
        return cls(amount, category, description, date, currency)

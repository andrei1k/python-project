from datetime import datetime
import copy
from functools import reduce

# the rate in the moment of writing
EURO_TO_LEV = 1,95
DOLLAR_TO_LEV = 1,80

class Expense:
    def __init__(self, amount: float,
                 category: str, description: str,
                 date: datetime=datetime.now(),currency: str='lv.') -> None:
        self.amount = amount
        self.category = category
        self.description = description
        self.date = date
        self.currency = currency
        
    def __str__(self) -> str:
        return f'Amount: {self.amount:.2f} {self.currency}\nCategory: {self.category}\nDescription: {self.description}\nDate: {self.date.strftime("%Y-%m-%d %H:%M:%S")}\n\n'
    
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

class Tracker:
    def __init__(self, expenses: list[Expense]=[], budget: float=0) -> None:
        self.expenses = copy.deepcopy(expenses)
        self.budget = budget

    def add(self, expense: Expense) -> None:
        self.expenses.append(copy.copy(expense))
        if not self.is_in_budget():
            print('You are over your budget!')
    
    def is_in_budget(self) -> bool:
        sum = reduce(lambda amount1, amount2: amount1 + amount2,
                     map(lambda expense: expense.amount, self.expenses))
        return sum < self.budget

    def sublist(self, start: datetime=datetime.min,
                end: datetime=datetime.now()) -> list[Expense]:
        sublist: list[Expense] = self.expenses
        sublist.sort(key = lambda expense: expense.date)
        return list(filter(lambda expense: expense.date >= start
                           and expense.date <= end, sublist))

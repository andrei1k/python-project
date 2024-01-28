from datetime import datetime
import copy

# the rate in the moment of writing
EURO_TO_LEV = 1,95
DOLLAR_TO_LEV = 1,80

class Expense:
    def __init__(self, amount: float,
                 category: str, description: str,
                 date: datetime=datetime.now(),currency: str='лв.') -> None:
        self.amount = amount
        self.category = category
        self.description = description
        self.date = date
        self.currency = currency

class Expenses:
    def __init__(self, expenses: list[Expense]=[]) -> None:
        self.expenses = copy.deepcopy(expenses)

    def add(self, expense: Expense) -> None:
        self.expenses.append(copy.copy(expense))

    def sublist(self, start: datetime=datetime.min,
                end: datetime=datetime.now()) -> list[Expense]:
        sublist: list[Expense] = self.expenses
        sublist.sort(key = lambda expense: expense.date)
        return list(filter(lambda expense: expense.date >= start
                           and expense.date <= end, sublist))

    # def csv(self)

from datetime import datetime
import copy

class Expense:
    def __init__(self, amount: float, type: str,
                 description: str, date: datetime) -> None:
        self.amount = amount
        self.type = type
        self.description = description
        self.date = date

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

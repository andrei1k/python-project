"""
This module implements class which saves the budget and expenses
and provides core functionality for working with them
"""
from datetime import datetime
import copy
from functools import reduce
from src.expense import Expense

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

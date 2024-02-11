'''
This module implements class which saves the budget and expenses
and provides core functionality for working with them
'''
from datetime import datetime
import copy
from functools import reduce
from src.expense import Expense

class Tracker:
    '''
    Represents an expense tracker that stores a list of expenses and a budget.

    :param expenses: list[Expense]
        A list of Expense objects representing existing expenses.
    :param budget: float, optional
        The budget for expenses. Defaults to 0.
    '''
    def __init__(self, expenses: list[Expense], budget: float=0) -> None:
        self.expenses = copy.deepcopy(expenses)
        self.budget = budget

    def add(self, expense: Expense) -> None:
        '''
        Adds an expense to the tracker and checks if it exceeds the budget.

        :param expense: An Expense object representing the expense to be added.

        :return: None
        '''
        self.expenses.append(copy.copy(expense))
        if not self.is_in_budget():
            print('You are over your budget!')

    def is_in_budget(self) -> bool:
        '''
        Checks if the total amount of expenses in the tracker is within the budget.

        :return: bool
        '''
        amount_sum = reduce(lambda amount1, amount2: amount1 + amount2,
                     map(lambda expense: expense.amount, self.expenses))
        return amount_sum < self.budget

    def sublist(self, start: datetime=datetime.min,
                end: datetime=datetime.now()) -> list[Expense]:
        '''
         Retrieves a sublist of expenses from the tracker based on the specified date range.

        :param start: datetime, optional
            The start date of the date range. Defaults to datetime.min.
        :param end: datetime, optional
            The end date of the date range. Defaults to the current date and time.

        :return: list[Expense]
        '''
        sublist: list[Expense] = self.expenses
        sublist.sort(key = lambda expense: expense.date)
        return list(filter(lambda expense: expense.date >= start
                           and expense.date <= end, sublist))

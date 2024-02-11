'''
This module contains unit tests for the Tracker class.
'''
from datetime import datetime
from src.expense import Expense
from src.tracker import Tracker

def test_tracker_creation():
    '''
    Test function to check the behavior of the add method in the Tracker class.
    '''
    current_time = datetime.now()
    sut = Tracker([Expense(1, 'food', 'it was yummy', current_time)])

    assert sut.budget == 0
    assert sut.expenses[0].amount == 1
    assert sut.expenses[0].category == 'food'
    assert sut.expenses[0].description == 'it was yummy'
    assert sut.expenses[0].date == current_time
    assert sut.expenses[0].currency == 'lv.'

def test_is_in_budget():
    '''
    Test function to check the behavior of the is_in_budget method in the Tracker class.
    '''
    tracker_within_budget = Tracker(expenses=[Expense(amount=50, category='Food',
                                                      description='Groceries',
                                                      date=datetime.now())], budget=100)
    assert tracker_within_budget.is_in_budget()

    tracker_exceeding_budget = Tracker(expenses=[Expense(amount=150, category='Entertainment',
                                                         description='Concert tickets',
                                                         date=datetime.now())], budget=100)
    assert not tracker_exceeding_budget.is_in_budget()

def test_add_expense_to_tracker():
    '''
    Test function to check the behavior of the add method in the Tracker class.
    '''
    tracker = Tracker(expenses=[], budget=100)
    expense_within_budget = Expense(amount=50, category='Food',
                                    description='Groceries', date=datetime.now())
    tracker.add(expense_within_budget)
    assert len(tracker.expenses) == 1
    assert tracker.is_in_budget()

    expense_exceeding_budget = Expense(amount=200, category='Entertainment',
                                       description='Concert tickets', date=datetime.now())
    tracker.add(expense_exceeding_budget)
    assert len(tracker.expenses) == 2
    assert not tracker.is_in_budget()

def test_sublist():
    '''
    Test function to check the behavior of the sublist method in the Tracker class.
    '''
    tracker = Tracker(expenses=[
        Expense(amount=50, category='Food',
                description='Groceries', date=datetime(2024, 2, 10)),
        Expense(amount=30, category='Transport',
                description='Bus fare', date=datetime(2024, 2, 11)),
        Expense(amount=20, category='Entertainment',
                description='Movie ticket', date=datetime(2024, 2, 12))
    ])
    start_date = datetime(2024, 2, 10)
    end_date = datetime(2024, 2, 11)
    result = tracker.sublist(start_date, end_date)
    assert len(result) == 2
    assert all(expense.date >= start_date and expense.date <= end_date for expense in result)

    start_date = datetime(2024, 2, 15)
    end_date = datetime(2024, 2, 20)
    result = tracker.sublist(start_date, end_date)
    assert len(result) == 0

    empty_tracker = Tracker([])
    start_date = datetime(2024, 2, 1)
    end_date = datetime(2024, 2, 28)
    result = empty_tracker.sublist(start_date, end_date)
    assert len(result) == 0

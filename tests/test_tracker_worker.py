'''
This module contains unit tests for the tracker_worker module.
'''
from datetime import datetime
import unittest.mock
from unittest.mock import patch
import builtins
import pytest
from src.tracker_worker import get_amount_from_user, get_date_from_user
from src.expense import Expense
from src.tracker import Tracker

from src.tracker_worker import TrackerWorker


def test_get_amount_from_user_positive():
    '''
    Test function to check the behavior of the get_amount_from_user function with a positive amount.
    '''
    with unittest.mock.patch.object(builtins, 'input', return_value='10'):
        assert get_amount_from_user() == 10

def test_get_amount_from_user_negative_then_positive():
    '''
    This test function checks the behavior of the get_amount_from_user function
    when provided with a negative amount followed by a positive amount.
    '''
    with unittest.mock.patch.object(builtins, 'input', side_effect=['-10', '10']):
        assert get_amount_from_user() == 10


def test_get_amount_from_user_non_numeric_then_positive():
    '''
    Test function to check the behavior of the get_amount_from_user
    function with non-numeric input followed by a positive amount.
    '''
    with unittest.mock.patch.object(builtins, 'input', side_effect=['abc', '10']):
        assert get_amount_from_user() == 10

def test_get_date_from_user_valid():
    '''
    Test function to check the behavior of the get_date_from_user function with a valid date input.
    '''
    with unittest.mock.patch('builtins.input', side_effect=['2024-02-10']):
        assert get_date_from_user() == datetime(2024, 2, 10)

def test_get_date_from_user_invalid_then_valid():
    '''
    Test function to check the behavior of the get_date_from_user function
    with an invalid date input followed by a valid date input.
    '''
    with unittest.mock.patch('builtins.input', side_effect=['abc', '2024-02-10']):
        assert get_date_from_user() == datetime(2024, 2, 10)

@pytest.mark.parametrize('inputs', [('10', 'food', 'test', '2024-02-10')])
def test_add_expense(inputs: list[str]):
    '''
    Test function to verify the behavior of the add_expense method in TrackerWorker.
    '''
    with patch('builtins.input', side_effect=inputs):
        tracker = Tracker([])
        tracker_worker = TrackerWorker(tracker)
        tracker_worker.add_expense()

        assert len(tracker.expenses) == 1
        assert tracker.expenses[0].amount == 10
        assert tracker.expenses[0].category == 'food'
        assert tracker.expenses[0].description == 'test'
        assert tracker.expenses[0].date == datetime(2024, 2, 10)

@pytest.mark.parametrize('inputs', ['20'])
def test_change_budget(inputs: list[str]):
    '''
    Test function to verify the behavior of the change_budget method in TrackerWorker.
    '''
    with patch('builtins.input', return_value=inputs):
        tracker = Tracker([])
        tracker_worker = TrackerWorker(tracker)
        tracker_worker.change_budget()

        assert tracker.budget == 20

@pytest.mark.parametrize('inputs', [('2024-01-01', '2024-12-31')])
def test_get_sublist(inputs: list[str]):
    '''
    Test function to verify the behavior of the get_sublist method in TrackerWorker.
    '''
    with patch('builtins.input', side_effect=inputs):
        tracker = Tracker([Expense(10, 'food', 'test', datetime(2024, 2, 10))])
        tracker_worker = TrackerWorker(tracker)
        sublist = tracker_worker.get_sublist()

        assert len(sublist) == 1
        assert sublist[0].amount == 10

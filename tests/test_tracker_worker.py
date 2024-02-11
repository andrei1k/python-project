from datetime import datetime
import os
from unittest.mock import patch, MagicMock
import builtins
from src.tracker_worker import get_amount_from_user, get_date_from_user
import pytest
from src.tracker_worker import TrackerWorker
from src.tracker import Tracker
from src.expense import Expense

@patch.object(builtins, 'input', side_effect=['10'])
def test_get_amount_from_user_positive(mock_input: MagicMock):
    assert get_amount_from_user() == 10
    
@patch.object(builtins, 'input', side_effect=['-10', '10'])
def test_get_amount_from_user_negative_then_positive(mock_input: MagicMock):
    assert get_amount_from_user() == 10

@patch.object(builtins, 'input', side_effect=['abc', '10'])
def test_get_amount_from_user_non_numeric_then_positive(mock_input: MagicMock):
    assert get_amount_from_user() == 10
    
@patch('builtins.input', side_effect=['2024-02-10'])
def test_get_date_from_user_valid(mock_input: MagicMock):
    assert get_date_from_user() == datetime(2024, 2, 10)

@patch('builtins.input', side_effect=['abc', '2024-02-10'])
def test_get_date_from_user_invalid_then_valid(mock_input: MagicMock):
    assert get_date_from_user() == datetime(2024, 2, 10)

@pytest.fixture
def mock_tracker() -> Tracker:
    return Tracker()

@patch('src.tracker_worker.get_amount_from_user', return_value=10.0)
@patch('builtins.input', side_effect=['category', 'expense description', '2024-02-10'])
def test_add_expense(mock_input: MagicMock, mock_get_amount_from_user: MagicMock, mock_tracker: Tracker) -> None:
    tracker_worker = TrackerWorker(mock_tracker)
    tracker_worker.add_expense()

    assert len(mock_tracker.expenses) == 1
    assert mock_tracker.expenses[0].amount == 10

@patch('src.tracker_worker.get_amount_from_user', return_value=100.0)
def test_change_budget(mock_get_amount_from_user: MagicMock, mock_tracker: Tracker) -> None:
    tracker_worker = TrackerWorker(mock_tracker)
    tracker_worker.change_budget()

    assert mock_tracker.budget == 100.0

@patch('src.tracker_worker.get_date_from_user', side_effect=[datetime(2024, 1, 1), datetime(2024, 12, 31)])
def test_view_sublist(mock_get_date_from_user: MagicMock, mock_tracker: Tracker) -> None:
    mock_tracker.sublist = MagicMock(return_value=[Expense(10.0, 'category', 'expense description', datetime(2024, 2, 10))])

    tracker_worker = TrackerWorker(mock_tracker)
    tracker_worker.view_sublist()

    mock_tracker.sublist.assert_called_once_with(datetime(2024, 1, 1), datetime(2024, 12, 31))

@patch('src.tracker_worker.input', side_effect=['test_tracker.txt'])
def test_save_tracker_existing_file(mock_input: MagicMock, mock_tracker: Tracker) -> None:
    tracker_worker = TrackerWorker(mock_tracker)
    tracker_worker.save_tracker()

    assert os.path.exists(os.path.join('outputs', 'test_tracker.txt'))
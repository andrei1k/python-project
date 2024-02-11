from datetime import datetime
from unittest.mock import patch, MagicMock
import builtins
from src.tracker_worker import get_amount_from_user, get_date_from_user

@patch.object(builtins, 'input', side_effect=['10'])  # Mocking user input
def test_get_amount_from_user_positive(mock_input: MagicMock):
    assert get_amount_from_user() == 10
    
@patch.object(builtins, 'input', side_effect=['-10', '10'])  # Mocking user input
def test_get_amount_from_user_negative_then_positive(mock_input: MagicMock):
    assert get_amount_from_user() == 10

@patch.object(builtins, 'input', side_effect=['abc', '10'])  # Mocking user input
def test_get_amount_from_user_non_numeric_then_positive(mock_input: MagicMock):
    assert get_amount_from_user() == 10
    
@patch('builtins.input', side_effect=['2024-02-10'])  # Mocking user input
def test_get_date_from_user_valid(mock_input: MagicMock):
    assert get_date_from_user() == datetime(2024, 2, 10)

@patch('builtins.input', side_effect=['abc', '2024-02-10'])  # Mocking user input
def test_get_date_from_user_invalid_then_valid(mock_input: MagicMock):
    assert get_date_from_user() == datetime(2024, 2, 10)
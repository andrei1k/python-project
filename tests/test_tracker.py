from datetime import datetime
from src.tracker import Expense, Tracker

def test_tracker_creation():
    
    current_time = datetime.now()
    sut = Tracker([Expense(1, 'food', 'it was yummy', current_time)])
    
    assert sut.expenses[0].amount == 1
    assert sut.expenses[0].category == 'food'
    assert sut.expenses[0].description == 'it was yummy'
    assert sut.expenses[0].date == current_time
    assert sut.expenses[0].currency == 'lv.'

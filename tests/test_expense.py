from datetime import datetime
from scr.expense import Expense, Expenses

def test_expenses_creation():
    
    current_time = datetime.now()
    sut = Expenses([Expense(1, 'food', 'it was yummy', current_time)])
    
    assert sut.expenses[0].amount == 1
    assert sut.expenses[0].category == 'food'
    assert sut.expenses[0].description == 'it was yummy'
    assert sut.expenses[0].date == current_time
    assert sut.expenses[0].currency == 'лв.'

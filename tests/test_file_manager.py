import os
from src.expense import Expense
from src.file_manager import save_tracker, read_tracker
from src.tracker import Tracker


def test_tracker_saving():
    tracker = Tracker([Expense(1, 'food', 'it was yummy'),
                       Expense(1234, 'rent', 'half of my pay check')], budget = 400)

    save_tracker(tracker, 'test1.txt')

    assert os.path.exists(os.path.join('outputs', 'test1.txt'))

def test_tracker_reading():
    sut = read_tracker('test1.txt')

    assert sut.budget == 400
    assert len(sut.expenses) == 2
    assert str(sut.expenses[0]) == str(Expense(1.00432, 'food', 'it was yummy'))
    assert str(sut.expenses[1]) == str(Expense(1234, 'rent', 'half of my pay check'))

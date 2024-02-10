import os
from src.expense import Expense
from src.tracker import Tracker
import csv


output_dir = './outputs'

def save_tracker(tracker: Tracker, file_name: str) -> None:
    try:
        with open(os.path.join(output_dir, file_name), 'w') as result_file:
            result_file.write(f'Budget: {tracker.budget}\n')
            result_file.writelines(map(str, tracker.expenses))
    except OSError as error:
        print(error)
        
def read_tracker(file_name: str) -> Tracker:
    tracker = Tracker()
    try:
        with open(os.path.join(output_dir, file_name)) as tracker_file:
            tracker.budget = float(tracker_file.readline().split(': ')[1])
            expenses = map(Expense.from_string, tracker_file.read().split('\n\n')[:-1])
            for expense in expenses:
                tracker.add(expense)
    except OSError as error:
        print(error)
        raise error
        
    return tracker

def export_as_csv(tracker: Tracker, file_name: str) -> None:
    data = map(lambda expense: expense.to_tuple(), tracker.expenses)
    file_path = os.path.join(output_dir, file_name)
    try:
        with open(file_path, 'w', newline='') as result_file:
            writer = csv.writer(result_file)
            writer.writerow(('Amount', 'Currency', 'Category', 'Description', 'Date'))
            writer.writerows(data)
    except OSError as error:
        print(error)

import os
from src.tracker import Expense, Tracker

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

"""
This module helps with reading data from the user input
and passing it to the current tracker
"""
from datetime import datetime
import os
from src.expense import Expense
from src.tracker import Tracker
from src.file_manager import export_as_csv, OUTPUT_DIR, save_tracker


def get_amount_from_user() -> float:
    while True:
        try:
            amount = float(input('Enter the amount: '))
            if amount < 0:
                raise ValueError
            break
        except ValueError:
            print('Amount should be float and positive.')

    return amount

def get_date_from_user(date_note: str='a') -> datetime:
    while True:
        try:
            date_str = input(f"Enter {date_note} date (YYYY-MM-DD): ")
            date = datetime.strptime(date_str, '%Y-%m-%d')
            return date
        except ValueError:
            print("Invalid date format.")

class TrackerWorker():
    def __init__(self, tracker: Tracker) -> None:
        self._tracker = tracker

    def add_expense(self) -> None:
        amount = get_amount_from_user()        
        category = input('Enter the category: ')
        description = input('Enter the description of the expense: ')
        date = get_date_from_user()

        self._tracker.add(Expense(amount, category, description, date))

        print('The expense was added!')

    def change_budget(self) -> None:
        budget = get_amount_from_user()
        self._tracker.budget = budget
        print('The budged was changed!')

    def view_sublist(self):
        start_date = get_date_from_user('start')
        end_date = get_date_from_user('end')

        sublist = self._tracker.sublist(start_date, end_date)

        for expense in sublist:
            print(str(expense))

    def save_tracker(self) -> None:
        name = input('Save as: ')
        rewrite = True
        if os.path.exists(os.path.join(OUTPUT_DIR, name)):
            if input('This tracker already exists. Do you want to rewrite it? [y/n] ') != 'y':
                rewrite = False

        file_format = name.split('.')[-1]

        if rewrite:
            try:
                if file_format == 'csv':
                    export_as_csv(self._tracker, name)
                elif file_format == 'txt':
                    save_tracker(self._tracker, name)
                else:
                    print('Invalid format (try .txt or .csv)')
                    return

                print('Tracker was saved!')
            except OSError:
                print('Tracker was NOT saved!')

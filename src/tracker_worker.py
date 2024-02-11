'''
This module helps with reading data from the user input
and passing it to the current tracker
'''
from datetime import datetime
import os
from src.diagram import save_diagram_by_categories, save_spending_graph
from src.expense import Expense
from src.tracker import Tracker
from src.file_manager import export_as_csv, OUTPUT_DIR, save_tracker


def get_amount_from_user() -> float:
    '''
    Prompts the user to enter a positive float value for an amount.

    :return: float
        The amount entered by the user.

    :raises ValueError:
        If the user input cannot be converted to a positive float value, a ValueError is raised.
    '''
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
    '''
    Prompts the user to enter a date in the format YYYY-MM-DD.

    :param date_note: str, optional
        A note to specify the purpose of the date entry (default is 'a').

    :return: datetime
        The datetime object corresponding to the date entered by the user.
    '''
    while True:
        try:
            date_str = input(f"Enter {date_note} date (YYYY-MM-DD): ")
            date = datetime.strptime(date_str, '%Y-%m-%d')
            return date
        except ValueError:
            print("Invalid date format.")

class TrackerWorker():
    '''
    This class encapsulates methods to perform various operations on an expense tracker

    Attributes:
        _tracker (Tracker): The expense tracker instance associated with the worker.
    '''
    def __init__(self, tracker: Tracker) -> None:
        self._tracker = tracker

    def add_expense(self) -> None:
        '''
        This method prompts the user to enter the 
        amount, category, description, and date of the expense,
        and then adds the expense to the tracker.

        :return: None
        '''
        amount = get_amount_from_user()
        category = input('Enter the category: ')
        description = input('Enter the description of the expense: ')
        date = get_date_from_user()

        self._tracker.add(Expense(amount, category, description, date))
        print('The expense was added!')

    def change_budget(self) -> None:
        '''
        This method prompts the user to enter a new budget amount,
        then updates the budget attribute of the expense tracker accordingly.

        :return: None
        '''
        budget = get_amount_from_user()
        self._tracker.budget = budget
        print('The budged was changed!')

    def get_sublist(self) -> list[Expense]:
        '''
        Retrieves a sublist of expenses from the tracker based on the specified date range.

        :return: list[Expense]
            A list containing expenses that fall within the specified date range.
        '''
        start_date = get_date_from_user('start')
        end_date = get_date_from_user('end')

        return self._tracker.sublist(start_date, end_date)

    def view_sublist(self) -> None:
        '''
        Displays the sublist of expenses from the tracker based on the specified date range.

        :return: None
        '''
        sublist = self.get_sublist()

        for expense in sublist:
            print(str(expense))

    def save_tracker(self) -> None:
        '''
        Saves the expense tracker to a file in either CSV or TXT format.

        :return: None
            This method does not return any value.
        '''
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

    def save_bar_plot_by_categories(self) -> None:
        '''
        Creates a bar plot as an html file for expenses 
        grouped by categories within the specified date range.

        :return: None
        '''
        sublist = self.get_sublist()
        save_diagram_by_categories(sublist)

    def save_line_plot(self) -> None:
        '''
        Creates a line plot as an html file for expenses within the specified date range.

        :return: None
        '''
        sublist = self.get_sublist()
        save_spending_graph(sublist)

'''
This module provides functionality working with files.
Saving and reading expenses from .txt files and saving as .csv
'''
import os
import csv
from src.expense import Expense
from src.tracker import Tracker

OUTPUT_DIR = './outputs'

def save_tracker(tracker: Tracker, file_name: str) -> None:
    '''
    Saves the budget and expenses from the given Tracker object to a txt file.

    :param tracker: Tracker
        The Tracker object containing the budget and expenses to be saved.
    :param file_name: str
        The name of the txt file to be created or overwritten.

    :return: None

    :raises OSError:
        If there is an issue with file handling, such as failure to open or write to the file,
        an OSError is raised with the details of the error.
    '''
    try:
        with open(os.path.join(OUTPUT_DIR, file_name), 'w', encoding='utf-8') as result_file:
            result_file.write(f'Budget: {tracker.budget}\n')
            result_file.writelines(map(str, tracker.expenses))
    except OSError as error:
        print(error)
        raise OSError from error

def read_tracker(file_name: str) -> Tracker:
    '''
    Reads expense data from a txt file and returns a Tracker object.

    :param file_name: str
        The name of the txt file to read from.

    :return: Tracker
        A Tracker object containing the budget and expenses read from the file.

    :raises OSError:
        If there is an issue with file handling, such as failure to open or read from the file,
        an OSError is raised with the details of the error.
    '''
    tracker = Tracker([])
    try:
        with open(os.path.join(OUTPUT_DIR, file_name), encoding='utf-8') as tracker_file:
            tracker.budget = float(tracker_file.readline().split(': ')[1])
            expenses = map(Expense.from_string, tracker_file.read().split('\n\n')[:-1])
            for expense in expenses:
                tracker.add(expense)
    except OSError as error:
        print(error)
        raise error

    return tracker

def export_as_csv(tracker: Tracker, file_name: str) -> None:
    '''
    Exports the expenses tracked in the given Tracker object to a CSV file.

    :param tracker: Tracker
        The Tracker object containing the expenses to be exported.
    :param file_name: str
        The name of the CSV file to be created or overwritten.

    :return: None

    :raises OSError:
        If there is an issue with file handling, such as failure to open or write to the file,
        an OSError is raised with the details of the error.
    '''
    data = map(lambda expense: expense.to_tuple(), tracker.expenses)
    file_path = os.path.join(OUTPUT_DIR, file_name)
    try:
        with open(file_path, 'w', newline='', encoding='utf-8') as result_file:
            writer = csv.writer(result_file)
            writer.writerow(('Amount', 'Currency', 'Category', 'Description', 'Date'))
            writer.writerows(data)
    except OSError as error:
        print(error)
        raise OSError from error

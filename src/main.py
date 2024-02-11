'''
This module provides functionality for managing
expenses and budgets through a command-line interface.
'''

from src.tracker import Tracker
from src.file_manager import read_tracker
from src.tracker_worker import TrackerWorker

def display_menu():
    '''
    Displays the menu options for interacting with the expense tracker.
    '''
    print('\nChoose the corresponding number')
    print('1. Add an expense')
    print('2. Set a budget')
    print('3. View expenses')
    print('4. Create statistics')
    print('5. Save current tracker')
    print('6. Export as csv file')
    print('7. Exit\n')

def read_one_or_two(option1: str, option2: str) -> str:
    '''
    Reads and validates the user's choice between two options.

    :param option1: The first option presented to the user.
    :param option2: The second option presented to the user.

    :return: The user's choice, either '1' or '2'.
    '''
    choice = ''
    while choice not in ['1', '2']:
        print('\nChoose 1 or 2')
        print(option1)
        print(option2)
        choice = input('Enter your choice: ')

    return choice

def main():
    '''
    Executes the main functionality of the expense tracker program.
    It prompts the user to choose between opening an existing tracker or starting a new one.
    Once a tracker is selected or created, the function enters a loop where it displays 
    a menu of options for interacting with the tracker and processes the user's input accordingly.

    :return: None
    '''
    print('Welcome to your expense tracker! Would you like to open existing tracker or start new?')
    choice = read_one_or_two('1. Open existing tracker', '2. Start new')
    tracker = Tracker([])

    while choice == '1':
        name = input('Enter the file name (.txt): ')
        if name.split('.')[-1] != 'txt':
            continue
        try:
            tracker = read_tracker(name)
            break
        except OSError:
            print('Could not read the file!')

    tracker_options = TrackerWorker(tracker)

    while True:
        display_menu()
        choice = input('Enter your choice: ')

        match choice:
            case '1':
                tracker_options.add_expense()
            case '2':
                tracker_options.change_budget()
            case '3':
                tracker_options.view_sublist ()
            case '4':
                choice = read_one_or_two('1. Line plot (date)', '2. Bar plot (categories)')
                if choice == '1':
                    tracker_options.save_line_plot()
                else:
                    tracker_options.save_bar_plot_by_categories()
            case '5':
                tracker_options.save_tracker()
            case '6':
                tracker_options.save_tracker()
            case '7':
                print('Exiting the program. Goodbye!')
                break
            case _:
                print('Invalid choice. Please enter a valid option.')

if __name__ == '__main__':
    main()

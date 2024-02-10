"""
This module provides functionality for managing
expenses and budgets through a command-line interface.

Functions:
- display_menu(): Displays a menu of options for interacting with the expense tracker.
- main(): The main function that runs the expense tracker application.
"""


from src.tracker import Tracker
from src.file_manager import read_tracker
from src.tracker_worker import TrackerWorker

def display_menu():
    print('Choose the corresponding number')
    print('1. Add an expense')
    print('2. Set a budget')
    print('3. View expenses')
    print('4. View statistics')
    print('5. Save current tracker')
    print('6. Export as csv file')
    print('7. Exit')

def main():
    print('Welcome to your expense tracker! Would you like to open existing tracker or start new?')
    choice = ''
    tracker = Tracker()

    while choice not in ['1', '2']:
        print('Choose 1 or 2')
        print('1. Open existing tracker')
        print('2. Start new')
        choice = input('Enter your choice: ')
        if choice == '1':
            name = input('Enter the file name: ')
            try:
                tracker = read_tracker(name)
                break
            except OSError:
                print('Could not read the file!')
                continue

        if choice == '2':
            break

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
                pass
                # option3(tracker)
            case '5':
                tracker_options.save_tracker()
            case '6':
                tracker_options.save_tracker_as_csv()
            case '7':
                print('Exiting the program. Goodbye!')
                break
            case _:
                print('Invalid choice. Please enter a valid option.')

if __name__ == '__main__':
    main()

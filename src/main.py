import os
from src.tracker import Expense, Tracker
from src.file_manager import output_dir, save_tracker, read_tracker
     
        
def display_menu():
    print('Choose the corresponding number')
    print('1. Add an expense')
    print('2. Set a budget')
    print('3. View expenses')
    print('4. View statistics')
    print('5. Save current tracker')
    print('6. Exit')

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

def option_add_expense(tracker: Tracker) -> None:
    amount = get_amount_from_user()        
    category = input('Enter the category: ')
    description = input('Enter the description of the expense: ')
    # date = input('Enter the date: ')
    
    tracker.add(Expense(amount, category, description))
    
    print('The expense was added!')

def option_change_budget(tracker: Tracker) -> None:
    budget = get_amount_from_user()
    tracker.budget = budget
    print('The budged was changed!')

# print('3. View expenses')
def option3(tracker: Tracker):
    print('You selected Option 3')
    # Add your functionality for Option 3 here

# print('6. Save current tracker')
def option_save_tracker(tracker: Tracker) -> None:
    name = input('Save as: ')
    rewrite = True
    if os.path.exists(os.path.join(output_dir, name)):
        if input('This tracker already exists. Do you want to rewrite it? [y/n] ') != 'y':
            rewrite = False
    
    if rewrite:
        save_tracker(tracker, name)
        
    print('Tracker was saved!')
            
            
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
                print('Coult nor read the file!')
                continue
            
        if choice == '2':
            break

        
    while True:
        display_menu()
        choice = input('Enter your choice: ')

        match choice:
            case '1':
                option_add_expense(tracker)
            case '2':
                option_change_budget(tracker)
            case '3':
                option3(tracker)
            case '4':
                option3(tracker)
            case '5':
                option_save_tracker(tracker)
            case '6':
                print('Exiting the program. Goodbye!')
                break
            case _:
                print('Invalid choice. Please enter a valid option.')

if __name__ == '__main__':
    main()
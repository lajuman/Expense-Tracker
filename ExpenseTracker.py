def add_expense(expenses, amount, category):
    expenses.append({'amount': amount, 'category': category})
    
def print_expenses(expenses):
    for expense in expenses:
        print(f'  Amount: {expense["amount"]},  Category: {expense["category"]}')
    
def total_expenses(expenses):
    return sum(map(lambda expense: expense['amount'], expenses))
    
def filter_expenses_by_category(expenses, category):
    return filter(lambda expense: expense['category'] == category, expenses)
    
def main():
    expenses = []
    while True:
        print('\n---------- Expense Tracker ----------')
        print('\nExpense Tracker')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Exit')
        
        choice = input('Enter your choice: ')

        if choice == '1':
            amount = float(input('\n  Enter amount: '))
            category = input('  Enter category: ')
            add_expense(expenses, amount, category)

        elif choice == '2':
            print('\n  All Expenses:')
            print_expenses(expenses)

        elif choice == '3':
            print('\n  Total Expenses: ', total_expenses(expenses))

        elif choice == '4':
            category = input('\n  Enter category to filter: ')
            print(f'\n  Expenses for {category}:')
            expenses_from_category = filter_expenses_by_category(expenses, category)
            print_expenses(expenses_from_category)

        elif choice == '5':
            print('  Exiting the program.')
            break
        print ('-'*40+'\n')
            
if __name__ == '__main__':
    main()


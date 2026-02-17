selection = input('enter your selection: 1. add income 2. add expense 3. view expenses 4. view income 5. view balance 6. save 7. exit: ')
expenses = {}
income = {}
while selection != '7':
    if selection == '1':
        try:
            inc_name = input('enter the source of your income: ')
            inc = float(input('enter your income: $'))
            if inc < 0:
                print('income cannot be negative')
                continue
            if inc_name in income:
                income[inc_name] += inc
            else:
                income[inc_name] = inc
        except ValueError:
            print('invalid input, please enter a number')
    elif selection == '2':
        try:
            exp_name = input('enter the name of your expense: ')
            expense = float(input('enter your expense: $'))
            if expense < 0:
                print('expense cannot be negative')
                continue
            if exp_name in expenses:
                expenses[exp_name] += expense
            else:
                expenses[exp_name] = expense
        except ValueError:
            print('invalid input, please enter a number')
    elif selection == '3':
        if not expenses:
            print('you have no expenses')
        else:
            print('your expenses are: $')
            for exp_name, expense in expenses.items():
                print(f'{exp_name}: ${expense:.2f}')
            print(f'your total expenses are: ${sum(expenses.values()):.2f}')
    elif selection == '4':
        if not income:
            print('you have no income')
        else:
            print('your income is: $')
            for inc_name, inc in income.items():
                print(f'{inc_name}: ${inc:.2f}')
            print(f'your total income is: ${sum(income.values()):.2f}')
    elif selection == '5':
        balance = sum(income.values()) - sum(expenses.values())
        print(f'your balance is: ${balance:.2f}')
    elif selection == '6':
        with open('budget.txt', 'w') as file:
            file.write('INCOME\n')
            for name, amount in income.items():
                file.write(f'{name},{amount}\n')

            file.write('EXPENSES\n')
            for name, amount in expenses.items():
                file.write(f'{name},{amount}\n')
        print('saved!')
    else:
        print('invalid selection')
    selection = input('enter your selection: 1. add income 2. add expense 3. view expenses 4. view income 5. view balance 6. save 7. exit: ')

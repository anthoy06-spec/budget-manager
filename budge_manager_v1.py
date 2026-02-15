selection = input('enter your selection: 1. add income 2. add expense 3. view expenses 4. view income 5. view balance 6. exit: ')
expenses = []
income = []
while selection != '6':
    if selection == '1':
        try:
            inc = float(input('enter your income: $'))
            income.append(inc)
        except ValueError:
            print('invalid input, please enter a number')
    elif selection == '2':
        try:
            expense = float(input('enter your expense: $'))
            expenses.append(expense)
        except ValueError:
            print('invalid input, please enter a number')
    elif selection == '3':
        if not expenses:
            print('you have no expenses')
        else:
            print('your expenses are: $')
            for expense in expenses:
                print(f'${expense:.2f}')
            print(f'your total expenses are: ${sum(expenses):.2f}')
    elif selection == '4':
        if not income:
            print('you have no income')
        else:
            print('your income is: $')
            for inc in income:
                print(f'${inc:.2f}')
            print(f'your total income is: ${sum(income):.2f}')
    elif selection == '5':
        balance = sum(income) - sum(expenses)
        print(f'your balance is: ${balance:.2f}')
    else:
        print('invalid selection')
    selection = input('enter your selection: 1. add income 2. add expense 3. view expenses 4. view income 5. view balance 6. exit: ')
import os
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

history = []
while True:
    clear()
    print(40 * '-')
    print('----PROFESSINAL CACULATOR----')
    print(40 * '-')

    print('''
1.Addition (+)
2.Subtraction (-)
3.Multiplication (*)
4.Division (/)
5.Power (**)
6.Modulus (%)
7.Show History
8.Exist
''')
    print(40 *'-')
    choice = input('choose an option :')
    if choice == '7':
        clear()

        print(40 * '-')
        print('---HISTORY---')
        print(40 * '-')
        if len(history) <= 0:
            print('history is empty')
        else:
            for item in history:
                print(item)
        input('\npress enter to continue')
        continue
    elif choice == '8':
        print('\ngoodbuy')
        break
    elif choice in ['1','2','3','4','5','6']:
        try:
            if choice == '1':
                sum = 0
                numbers = input('enter number :').split()
                for number in numbers:
                    sum += float(number)
                    history.append(sum)
                print(f'sum numbers : {sum}')
                    
            elif choice =='2':
                numbers = input('enter number :').split()
                Subtraction = float(numbers[0])
                for number in numbers[1:]:
                    Subtraction -=  float(number)
                    history.append(Subtraction)
                print(f'Subtraction numbers : {Subtraction}')

                    
            elif choice =='3':
                Multiplication = 1
                numbers = input('enter number :').split()
                for number in numbers:
                    Multiplication *=  float(number)
                    history.append(Multiplication)
                print(f'Multiplication numbers : {Multiplication}')

                    
            elif choice =='4':
                numbers = input('enter number :').split()
                Division  =float(numbers[0])
                if numbers[0] == '0':
                    print('error cont divide by zero!')
                    print('press enter to continue..')
                else:
                    for number in numbers[1:]:
                    
                        Division  /=  float(number)
                        history.append(Division )
                    print(f'Division  numbers : {Division }')

            elif choice =='5':
                Power = 1
                numbers = input('enter number :').split()
                for number in numbers:
                    Power **=  float(number)
                    history.append(Power)
                print(f'Power numbers : {Power}')

            elif choice =='6':
                Modulus = 0
                numbers = input('enter number :').split()
                for number in numbers:
                    Modulus %=  float(number)
                    history.append(Modulus)
                print(f'Modulus numbers : {Modulus}')

        except ValueError:
            print('\ninvalid input!')
        input('\npress enter to continue...')

    else:
        print('invalid choice')
                    
                





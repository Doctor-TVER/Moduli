score_sum = 0
history = []
while True:
    print('1. пополнение счета')
    print('2. покупка')
    print('3. история покупок')
    print('4. выход')
    print(f'На вашем счете {score_sum}')

    choice = input('Выберите пункт меню')
    if choice == '1':
        cost = int(input('Введите сумму пополнения: '))
        score_sum += cost
    elif choice == '2':
        score_sum = buy(score_sum)
    elif choice == '3':
        print(history)
    elif choice == '4':
        break
    else:
        print('Неверный пункт меню')
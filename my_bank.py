# score_sum = 0
# history = []
# while True:
#     print('1. пополнение счета')
#     print('2. покупка')
#     print('3. история покупок')
#     print('4. выход')
#     print(f'На вашем счете {score_sum}')
#
#     choice = input('Выберите пункт меню')
#     if choice == '1':
#         cost = int(input('Введите сумму пополнения: '))
#         score_sum += cost
#     elif choice == '2':
#         score_sum = buy(score_sum)
#     elif choice == '3':
#         print(history)
#     elif choice == '4':
#         break
#     else:
#         print('Неверный пункт меню')

"""
МОДУЛЬ 3
Программа "Личный счет"
Описание работы программы:
Пользователь запускает программу у него на счету 0
Программа предлагает следующие варианты действий
1. пополнить счет
2. покупка
3. история покупок
4. выход

1. пополнение счета
при выборе этого пункта пользователю предлагается ввести сумму на сколько пополнить счет
после того как пользователь вводит сумму она добавляется к счету
снова попадаем в основное меню

2. покупка
при выборе этого пункта пользователю предлагается ввести сумму покупки
если она больше количества денег на счете, то сообщаем что денег не хватает и переходим в основное меню
если денег достаточно предлагаем пользователю ввести название покупки, например (еда)
снимаем деньги со счета
сохраняем покупку в историю
выходим в основное меню

3. история покупок
выводим историю покупок пользователя (название и сумму)
возвращаемся в основное меню

4. выход
выход из программы

При выполнении задания можно пользоваться любыми средствами
"""


def run_bill():
    """
    Функция запускает программу личный счет
    :return:
    """
    import os

    BUY_NAME = 'orders.txt'
    BILL_NAME = 'bill_sum.txt'

    history = []

    if os.path.exists(BUY_NAME):
        with open(BUY_NAME, 'r') as f:
            for order in f:
                history.append(order.replace('\n', ''))
    if os.path.exists(BILL_NAME):
        with open(BILL_NAME, 'r') as b:
            bill_sum = int(b.read())
    else:
        bill_sum = 0


    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')
        print(f'Ваш счет {bill_sum}')

        choice = input('Выберите пункт меню')
        if choice == '1':
            cost = int(input('Введите сумму'))
            bill_sum += cost
        elif choice == '2':
            cost = int(input('Введите сумму покупки'))
            if cost > bill_sum:
                print('Недостаточно средств')
            else:
                bill_sum -= cost
                name = input('Введит название покупки')
                history.append((name, cost))
        elif choice == '3':
            print(history)
        elif choice == '4':
            with open(BUY_NAME, 'w') as f:
                for order in history:
                    f.write(f'{order}\n')
            with open(BILL_NAME, 'w') as b:
                    b.write(f'{bill_sum}')
            break
        else:
            print('Неверный пункт меню')

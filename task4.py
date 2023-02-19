def check(list):
    if len(list) == 6:
        return False
    return True

guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
while True:
    print('Сейчас на вечеринке', len(guests), 'человек:', guests)
    command = input('Гость пришёл или ушёл? ')
    if command == 'пришел':
        name = input('Имя гостя: ')
        if check(guests) == True:
            guests.append(name)
            print('Привет,', name + '!', end='\n\n')
        else:
            print('Прости,', name + ', но мест нет.', end='\n\n')
    elif command == 'ушел':
        name = input('Имя гостя: ')
        if name in guests:
            guests.remove(name)
            print('Пока,', name + '!', end='\n\n')
        else:
            print('Такого гостя нет.', end='\n\n')
    elif command == 'Пора спать':
        print('\nВечеринка закончилась, все легли спать.')
        break
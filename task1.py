main = [1, 5, 3]
additional_list_1 = [1, 5, 1, 5]
additional_list_2 = [1, 3, 1, 5, 3, 3]

main.extend(additional_list_1)

print('Кол-во цифр 5 при первом объединении:', main.count(5))

for _ in range(main.count(5)):
    main.remove(5)

main.extend(additional_list_2)

print('Кол-во цифр 3 при втором объединении:', main.count(3))
print('Итоговый список:', main)
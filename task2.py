def sort(list):
    for i in range(len(list) - 2):
        for j in range(i + 1, len(list) - 1, 1):
            if list[i] > list[j]:
                list[i], list[j] = list[j], list[i]

first_form = []
second_form = []

for i in range(160, 177, 2):
    first_form.append(i)

for i in range(162, 181, 3):
    second_form.append(i)

first_form.extend(second_form)

sort(first_form)

print('Отсортированный список учеников:', first_form)
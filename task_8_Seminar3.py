'''
Погружение в Python (семинары)
Урок 3. Коллекции

1.Решить задачи, которые не успели решить на семинаре.

Задание №8

✔ Три друга взяли вещи в поход. Сформируйте  словарь, где ключ — имя друга, а значение — кортеж вещей. 

Ответьте на вопросы:

✔ Какие вещи взяли все три друга

✔ Какие вещи уникальны, есть только у одного друга

✔ Какие вещи есть у всех друзей кроме одного  и имя того, у кого данная вещь отсутствует

✔ Для решения используйте операции  с множествами. Код должен расширяться на любое большее количество друзей.
'''
########################
#Task 8 Lesson 3. СЕМИНАР

data = {'Ваня': ('нож', 'чай', 'спички', 'компас', 'фонарь'),
        'Петя': ('вода', 'нож', 'спички', 'палатка', 'компас'),
        'Миша': ('нож', 'консервы', 'сахар', 'ложка', 'топор')}


common = set()

for i in data.values():
    for j in i:
        common.add(j)

print('Tри друга вместе взяли: ', common)

print('Уникальные вещи у каждого:')
for person in data:
    others = tuple(pers for pers in data.keys() if pers != person)
    things = set(item for item in (items for key in others for items in data[key]))
    unique = set(data[person]).difference(things)
    if unique:
        print(f'{person}: {unique}')

for person in data:
    others = tuple(pers for pers in data.keys() if pers != person)
    things = set(item for item in (items for key in others for items in data[key]))
    absent = things.difference(set(data[person]))

    if absent:
        print(f'{person} не имеет {absent}')
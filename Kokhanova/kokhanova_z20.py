'''Капитан Флинт зарыл клад на Острове сокровищ. Он оставил описание, как найти
клад. Описание состоит из строк вида: "North 5", где слово – одно
из "North", "South", "East", "West", – задает направление движения, а число –
количество шагов, которое необходимо пройти в этом направлении.
Напишите программу, которая по описанию пути к кладу определяет точные
координаты клада, считая, что начало координат находится в начале пути, ось OX
направлена на восток, ось OY – на север.'''
x = y = 0
s = input()
while s:
    s = s.split()
    s[1] = int(s[1])
    if s[0] == "North":
        y += s[1]
    elif s[0] == "South":
        y -= s[1]
    elif s[0] == "East":
        x += s[1]
    elif s[0] == "West":
        x -= s[1]
    else:
        print('Не знаю такого направления')
    s = input()
print(x, y)
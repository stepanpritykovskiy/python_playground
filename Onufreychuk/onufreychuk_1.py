"""
Заполните один кортеж десятью случайными целыми числами от 0 до
5 включительно. Также заполните второй кортеж случайными числами
от -5 до 0. Для заполнения кортежей числами напишите одну функцию.
Объедините два кортежа с помощью оператора +, создав тем самым
третий кортеж. С помощью метода кортежа count() определите в нем
количество нулей. Выведите на экран третий кортеж и количество нулей
в нем. Определите первое и второе вхождения числа 0 в кортеж
"""
from random import randint
a1=tuple(randint(0,5)for i in range (10))
a2=tuple(randint(-5,0)for i in range (10))
a3=a1+a2
kolvo=a3.count(0)
kol1=a3.index(0)
srez=kol1+1 #делаем срез кортежа (начиная с первого вхождения '0')
srez_a3=a3[srez:-1]
kol2=srez_a3.index(0)
print(a3)
print("Кол-во нулей: ",kolvo)
print("Первое вхождение (0) в кортеж: ",kol1+1)
print("Второе вхождение (0) в кортеж : ",kol1+kol2+2)

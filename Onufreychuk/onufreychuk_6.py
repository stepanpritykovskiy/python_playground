"""
Каждый из N школьников некоторой школы знает Mi языков. Определите, какие
языки знают все школьники и языки, которые знает хотя бы один из
школьников.
Первая строка входных данных содержит количество школьников N. Далее
идет N чисел Mi, после каждого из чисел идет Mi строк, содержищих названия
языков, которые знает i-й школьник. Длина названий языков не превышает 1000й школьник. Длина названий языков не превышает 1000
символов, количество различных языков не более 1000. 1≤N≤1000, 1≤Mi≤500.
"""
language = []
some = set()
obshee = set()
for a in range(int(input())):
    v = int(input())
    a = {input() for j in range(v)}
    obshee.update(a)
    if len(some) ==0:
        some.update(a)
    else:
        some&=a
print(len(some))
print('\n'.join(sorted(some)))
print(len(obshee))
print('\n'.join(sorted(obshee)))
"""
Даны два списка чисел, которые могут содержать до 10000 чисел
каждый. Выведите все числа, которые входят как в первый, так и во
второй список в порядке возрастания.
"""
a1=input("Введите первый список чисел: ").split()
a2=input("Введите второй список чисел: ").split()
a1=set(a1)
a2=set(a2)
peresechenie=a1.intersection(a2)
otvet=sorted(peresechenie)
print("Все числа, которые входят как в первый, так и во второй список в порядке возрастания:",otvet) 
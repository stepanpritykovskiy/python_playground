"""Найдите количество элементов массива, которые отличны от наибольшего элемента не более
чем на 10%."""
n=list(map(int,input().split()))
a=max(n)
c=0
for i in n:
    if i+(a*0.1)>=a:
        c=c+1
print(c-1)        
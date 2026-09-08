def carp(x):
    return x*2

numbers = [1,2,3,4,5]
result = map(carp, numbers)
print(list(result))


list1 = [7,3,5]
list2 = [34,83,4]
result2 = map(lambda x,y: x+y, list1, list2) #* forEach gibi bir döngüdür, her elemanı teker teker döner
print(list(result2))


#? filter sınıfı

liste = [1,2,3,4,5,6,7,8]
sonuc = filter(lambda x: x%2 == 0, liste) #* koşula uyanları filtereler
print(list(sonuc))


#? sorted metotu

rslt = sorted(liste,reverse=True) #* büyükten küçüğe sıralar
print(list(rslt))

degerler = [1,7,-2,-8,4]
a = sorted(degerler,key=lambda x: abs(x)) #* eksiler artıymış gibi sıralama yapmasını sağladık
print(list(a))


#? fonksiyon içi lambda

def my_function(n):
    return lambda x: x*n

r = my_function(4)
print(r(15))
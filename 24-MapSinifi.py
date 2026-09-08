 #? map
#* Her iterable'ın elemanlarını tek tek işleyerek yeni bir iterator döndürür.
#* 1.parametre fonksiyon, 2.parametre iterable, 3. 4. ... olarak da birden fazla iterable gönderilebilir

def carp(x):
    return x * 2

numbers = [1,2,3,4,5]
result = map(carp, numbers)
print(list(result))

# def carp(numbers):
#     return [number * 2 for number in numbers]  
# numbers = [1,2,3,4,5]
# print(carp(numbers))

#* Aynı işlevi görür


list1 = [7,3,5]
list2 = [34,83,4]
result2 = map(lambda x,y: x+y, list1, list2) 
print(list(result2))


#? Filter Sınıfı
#* map gibi tüm elemanları işler, koşula uyanları getirir

liste = [1,2,3,4,5,6,7,8]
sonuc = filter(lambda x: x % 2 == 0, liste) 
print(list(sonuc))


#? Sorted Metotu

rslt = sorted(liste, reverse = True) #* büyükten küçüğe sıralar
print(rslt)

degerler = [1,7,-2,-8,4]
a = sorted(degerler, key = lambda x: abs(x)) #* eksiler artıymış gibi sıralama yapmasını sağlar
print(a)


#? Fonksiyon İçi Lambda

def my_function(n):
    return lambda x: x * n

r = my_function(4)
print(r(15))
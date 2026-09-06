# fruit = ["Graphe","Orange","Strawberry","Pineapple","Melon","Matermelon"]+["cherry","apple"]

fruit = ["Graphe","Orange","Strawberry","Pineapple","Melon","Matermelon"]
fruit2 = ["Armut","Ayva","Hurma"]

#? copy()
newfruit = fruit2.copy() #* sığ (shallow) kopya oluşturur
#! iç içe mutable nesneler varsa alt nesneler iki listede paylaşılır

#? append(eklenecek_eleman)
fruit.append("cherry") #* append elemanı sona ekler

#? insert(eklenecek_index, eklenecek_eleman)
fruit.insert(1,"lemon") #* insert 1.parameteredeki endekse 2.parametredeki değeri atar

#? extend()
fruit.extend(fruit2) #* fruit'e fruit2'yi ekler
print("fruit.extend(fruit2) =>",fruit) 

#? pop(index)
fruit2.pop() #* elemanı siler (default:-1 index)
print("fruit2.pop() =>",fruit2)

#? remove(silinecek_eleman)
newfruit.remove("Ayva") #* parametre içine değer girerek bir ya da birkaç öğeyi silebiliriz

#? clear()
fruit.clear() #* fruit'in içindeki verileri siler

#?
del fruit #* fruit'i komple siler

esyalar = ["sandalye","masa","tahta","kaşık","tabak","sıra"]

#? sort()
esyalar.sort() #* sort(): küçükten büyüğe , a'dan z'ye sıralar 
print(esyalar) 

#? reverse()
esyalar.reverse() #* diziyi tersine çevirir (0->-1,1->-2)index
print(esyalar) 

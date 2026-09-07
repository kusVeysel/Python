 #? Liste Metotları

#* copy(): Sığ (shallow) kopya oluşturur
#! İç içe mutable nesneler varsa alt nesneler iki listede paylaşılır.

#* append(): Elemanı listenin sonuna ekler

#* insert(x, y): Belirtilen index'e eleman ekler
# → x: Index numarası
# → y: Eklenecek eleman

#* extend(): Listenin sonuna başka bir iterable'ın elemanlarını ekler
# → Genellikle iki listeyi birleştirmek için kullanılır.

#* pop(): Belirtilen index'teki elemanı siler ve geri döndürür, default olarak -1
# → Index verilmezse son elemanı siler.

#* remove(): Belirtilen değere sahip ilk elemanı siler
#! Aynı elemandan birden fazla varsa sadece ilk eşleşeni(index'İ küçük olan) siler.

#* clear(): Listenin içindeki tüm elemanları siler
# → Liste tamamen boşaltılır.

#* del: Belirtilen elemanı, index aralığını veya liste değişkenini silebilir
# → del liste[0]
# → del liste[1:4]
# → del liste

#* sort(): Listeyi varsayılan olarak küçükten büyüğe / A'dan Z'ye sıralar
# → reverse = True → Büyükten küçüğe / Z'den A'ya
# → key = → Sıralama kriteri belirlemek için kullanılır.

#* reverse(): Listenin elemanlarının sırasını tersine çevirir
# → İlk eleman son, son eleman ilk olur.


fruit = ["Elma","Armut"]
fruit2 = ["Karpuz","Ayva"]

print("fruit →",fruit)
print("fruit2 →",fruit2)

#? copy()
print("------------------------------------------")
newFruit = ["Karpuz","Ayva"].copy()
print("newFruit = ['Karpuz','Ayva'].copy() →", newFruit)
print("------------------------------------------")

#? append()
newFruit.append("Kiraz")
print('newFruit.append("Kiraz") →',newFruit)
print("------------------------------------------")

#? insert()
newFruit.insert(1,"Limon")
print('newFruit.insert(1,"Limon") →',newFruit)
print("------------------------------------------")

#? extend()
fruit.extend(fruit2)
print('fruit.extend(fruit2) →',fruit)
print("------------------------------------------")

#? pop()
silinen = newFruit.pop()
print(f'newFruit.pop() →  {newFruit}, silinen eleman → {silinen}')
print("------------------------------------------")

#? remove()
newFruit.remove("Karpuz")
print('newFuit.remove("Elma") →', newFruit)
print("------------------------------------------")

#? clear()
newFruit.clear()
print('newFruit.clear() →',newFruit)
print("------------------------------------------")

#?
del newFruit

#? sort()
fruit.sort()
print('fruit.sort() →',fruit) 
print("------------------------------------------")

#? reverse()
fruit.reverse()
print("fruit.reverse() →",fruit) 
print("------------------------------------------")

# fruit = ["Graphe","Orange","Strawberry","Pineapple","Melon","Matermelon"]+["cherry","apple"]
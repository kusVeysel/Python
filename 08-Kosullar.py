sayi1 = 10
sayi2 = 5

if sayi1>sayi2:
    print("Sayi1 daha büyüktür")
elif sayi1==sayi2:
    print("Sayi1 sayi2'ye eşittir")
else:
    print("Sayi1 daha küçüktür")

#! Boşluklara düzene dikkat normalde programlama dillerinde önemlidir ama python'da daha önemlidir

x = bool("python")
y = bool(7)
print(x,y)
print(type(x),type(y))
# None, False, 0 ve boş string/list/tuple/set/dict değerleri False kabul edilir.

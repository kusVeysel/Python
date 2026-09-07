 #? tuple
#* Sıralıdır: Kod her çalıştığında veriler hangi sırayla yazıldıysa öyle gelir
#* Değiştirilemez: Veriler değiştirilemez
#* Yinelenebilir: Aynı veri tekrar kullanılabilir


fruits = ("çilek","armut","elma","ayva","muz") # tuple veri türü
fruits1= ("karpuz",) # tuple veri türü
fruits2 = ("kavun") # string veri türü

print(type(fruits),type(fruits1),type(fruits2))

#? *n : elemanların verilerini n kadar tekrar yazar
print(fruits * 2)

x,y,*z = fruits #! destruct
#! * (rest/spread operatörü) = accumulator (biriktiricidir)

print(x)
print(y)
print(z)

#? tuple
#* Sıralıdır: Kod her çalıştığında veriler hangi sırayla yazıldıysa öyle gelir
#* Değiştirilemez: Veriler değiştirilemez
#* Yinelenebilir: Aynı veri kullanılabilir


fruits = ("çilek","armut","elma","ayva","muz")
fruits1= ("karpuz",) #* tuple veri turu
fruits2 = ("kavun") #* string veri turu

print(type(fruits1),type(fruits2))

#? *n : elemanların verilerini n kadar tekrar yazar
print(fruits*2)

x,y,*z = fruits #! destruct
#! * = ... (rest/spread opeeratörü) javascript'in önemli bir operatörüdür ,acc yani biriktiricidir

print(x)
print(y)
print(z)
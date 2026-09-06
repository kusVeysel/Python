import random 

#? random()
print(random.random()) #* 0 ile 1 (1 dahil değil) arasında sayı üretir

#? seed()
random.seed() #* üretecin durumunu sistem rastgeleliğiyle ayarlar; aynı tohum aynı diziyi üretir
print(random.random())

#? getstate()
state = random.getstate() #* sonraki random sayıyı tut
random.random() #* bunu state değişkeni tutar

random.setstate(state) #* 12.satırda üretilen sayı ile aynı sayıyı verir

#? getrandbits(BitBoyutu)
print(random.getrandbits(8)) #* 8 bit boyutunda sayı üretir(0-255)

#? randrange(BaşlangıçDeğeri, BitişDeğeri(DahilDeğil),ArtışMiktarı)
print(random.randrange(1,20,3))
#* 3.parametreden dolayı : 1,4,7,10,13,16,19 sayıları üretir

#? randint(BaşlangıçDeğeri, BitişDeğeri)
print(random.randint(1,10))

#? choices(seri) liste,string,tuple vs.
myList = ["wihte","red","green","yellow","black"]
print(random.choice(myList)) #* Diziden rastgele bir eleman döndürür

#? choices(Seri,weights=[GelmeOranı],k=ListeKaçAdet)
myList2 = ["cherry","strawberry","graphe","banana","apple"]
print(random.choices(myList2,weights=[10,3,5,1,1],k=20))

#? shuffle(Seri)
myList3 = ["skoda","bmw","audi","nissan","toyota","hundai","volvo"]
random.shuffle(myList3) #* Verilen dizinin elemanlarını rastgele karıştırır
print(myList3)

#? sample(Seri,k=adet)
print(random.sample(myList3,k=3)) #* Verilen diziden tekrarsız 3 adet yeni dizi döner

#? uniform(BaşlangıçDeğeri,BitişDeğeri)
print(random.uniform(10,30)) #* 10 ile 30 arasında(dahil) rastgele ondalıklı sayı üretir

#? triangular(BaşlangıçDeğeri,BitişDeğeri,mode)
#* mode => kime yakınsa o sayıya yakın sayılar üretir
print(random.triangular(10,30,10))

print("\n------Belirli Dağılımlara Göre Float Sayı Üreten Fonksiyonlar------")

#? betavariate(alpha,beta)
#* Büyük alpha dağılımı 1'e, büyük beta dağılımı 0'a doğru yoğunlaştırır
print(random.betavariate(6,2)) #* beta 1'e daha yakın , alpha 0'a uzak yani 1'e daha yakın sayılar üretir

#? expovariate()
#* Üstel dağılıma göre rastgele sayı döndürür
print(random.expovariate(1.0)) #* lambd zorunludur; 1.0 oranını kullanır

#? gammavariate
#* Normal (Gaussian) dağılıma göre rastgele sayı döndürür
print(random.gammavariate(110,2))

#? gauss()
#* Gama dağılıma göre rastgele sayı döndürür
print(random.gauss(200,50))

#? lognormvariate()
#* Log-normal dağılıma göre rastgele sayı döndürür
print(random.lognormvariate(0,0.25))

#? normalvariate()
#* Normal dağılıma göre rastgele sayı döndürür
print(random.normalvariate(100,50))

#? vonmisesvariate()
#* Von Mises(dairesel normal) dağılıma göre rastgele sayı döndürür
print(random.vonmisesvariate(0,5))

#? paretovariate()
#* Pareto dağılıma göre rastgele sayı döndürür
print(random.paretovariate(3))

#? weibullvariate()
#* Weibull dağılıma göre rastgele sayı döndürür
print(random.weibullvariate(1,1.5))
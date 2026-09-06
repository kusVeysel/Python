
#* if-else'in ternary operatörü gibi lambda fonksiyonlar da fonksiyonların kısa yazımı

#! python için ternary operator yazılımı
#! degişken = koşul_doğruysa if koşul else koşul_yanlışsa

#! başka kullanım (iki dal da önce değerlendirilir; kısa devre için ternary expression kullanın)
#! degişken = (koşul_yanlışsa, koşul_doğruysa)[koşul] 

sayi = 0
a = "pozitif" if sayi>10 else "pozitif değil"
print(a)
d = ("pozitif değil","pozitif")[sayi>0]

result = lambda x: x+10

# def result(x):
#     return x+10    
#* aynısıdır

print(result(9))

kontrol = lambda sayi: "pozitif" if sayi>0  else "pozitif değil"

print(kontrol(int(input("Bir Sayı Giriniz: "))))
sayi1 = 10
sayi2 = 5

if sayi1 > sayi2:
    print("sayi1 daha büyüktür")
elif sayi1 == sayi2:
    print("sayi1 sayi2'ye eşittir")
else:
    print("sayi1 daha küçüktür")

#! Boşluklara düzene dikkat normalde programlama dillerinde önemlidir ama python'da daha önemlidir


#* Ternary Operatörü 

#! python için ternary operator yazılımı
#! degişken = koşul_doğruysa if koşul else koşul_yanlışsa

#! başka kullanım (iki dal da önce değerlendirilir; kısa devre için ternary expression kullanın)
#! degişken = (koşul_yanlışsa, koşul_doğruysa)[koşul] 

sayi = 0

a = "pozitif" if sayi>10 else "pozitif değil"
print(a)

d = ("pozitif değil","pozitif")[sayi>0]

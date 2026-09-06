import math

#? Sabitler
print("-----Sabitler-----")
print("math.e =>",math.e)
print("math.inf =>",math.inf)
print("-math.inf =>",-math.inf)
print("math.nan =>",math.nan)
print("math.pi =>",math.pi)
print("math.tau =>",math.tau)

#? Açılar
print("-----Açılar-----")
print("math.acos(0.55) =>",math.acos(0.55))
print("math.acosh(7) =>",math.acosh(7))
print("math.asin(0.55 =>",math.asin(0.55))
print("math.asinh(7) =>",math.asinh(7))
print("math.atan(0.4) =>",math.atan(0.4))
print("math.atan2(8,5) =>",math.atan2(8,5))
print("math.atanh(0.59) =>",math.atanh(0.59))

#?
print()
print("math.degrees(8.9) =>",math.degrees(8.9)) #* radyanı dereceye çevirir
print("math.radians(180) =>",math.radians(180)) #* dereceyi radyana çevirir

#? 
print()
print("math.ceil(1.1) =>",math.ceil(1.1)) #* bi üst tam sayıya yuvarlar
print("math.floor(1.9) =>",math.floor(1.9)) #* bi alt tam sayıya yuvarlar
print("math.sqrt(10) =>",math.sqrt(10)) #* karakökü alır
print("math.isqrt(10) =>",math.isqrt(10)) #* karakökü alır ama int, yani sqrt + floor gibi
print("math.trunc(45.7438057) =>",math.trunc(45.7438057)) #* ondalıklı kısmını atar
print("math.remainder(19,4) =>",math.remainder(19,4)) #* 1.parametrenin 2.parametreye bölümünü verir
#* dönen_değer = 1.parametre - (bölümün yüksek en yakın tam sayısı(ceil) * 2.parametre)

#?
print()
print("math.comb(7,4) =>",math.comb(7,4)) #* kombinasyon alır
print("math.copysign(7,-19) =>",math.copysign(7,-19)) #* 1.parametrenin değerini 2.parametrenin işaretini alır 
p = [3,3]
q = [6,7]
print("math.dist(p,q) =>",math.dist(p,q)) #* 2 nokta arası mesafeyi hesaplar
print("math.erf(0.7) =>",math.erf(0.7))
print("math.erfc(0.7) =>",math.erfc(0.7))
#* erf(x) + erfc(x) = 1
print("math.exp(1) =>",math.exp(1)) #* e üzeri 1.parametre(1) 
print("math.expm1(1) =>",math.expm1(1)) #* e üzeri 1.parametre(1) 
#* exp() ve expm1() arsındaki fark expm1() hassas ölçümler için daha iyidir
print("math.exp2(1) =>",math.exp2(1)) #* 2 üzeri 1.parametre(1)

#?
print()
print("math.fabs(-7) =>",math.fabs(-7)) #* mutlak değer alır
print("math.factorial(7) =>",math.factorial(7)) #* faktöriyel alır
print("math.fmod(19,4) =>",math.fmod(19,4)) #* 1.parametrenin 2.parametreye bölümünden kalanı verir
print("math.frexp(19) =>",math.frexp(19)) #* 1.parametreyi 2^x * y şeklinde verir
print("math.fsum([1,2,3,4,5]) =>",math.fsum([1,2,3,4,5])) #* float tipinde toplam alır
print("math.gamma(7) =>",math.gamma(7)) #* gamma fonksiyonu
print("math.lgamma(7) =>",math.lgamma(7)) #* gamma fonksiyonunun logaritmasını alır
print("math.prod([19,4]) =>",math.prod([19,4])) #* içindeki sayıların çarpımını verir

#?
print()
print("math.gcd(19,4) =>",math.gcd(19,4)) #* 1.parametre ile 2.parametrenin en büyük ortak bölenini verir
print("math.hypot(3,4) =>",math.hypot(3,4)) #* 2 parametreyi hipotenüs olarak kabul edip hipotenüsü verir
print("math.isclose(0.1+0.2,0.3) =>",math.isclose(0.1+0.2,0.3)) #* 2 parametreyi birbirine yakın mı diye kontrol eder
print("math.isfinite(7) =>",math.isfinite(7)) #* sonlu olup olmadığını kontrol eder
print("math.isinf(7) =>",math.isinf(7)) #* 1.parametre sonsuz mu diye kontrol eder
print("math.isnan(7) =>",math.isnan(7)) #* 1.parametre nan mı diye kontrol eder
print("math.frexp(10) =>",math.frexp(10)) #* 1.parametreni 2^x * y şeklinde verir
print("math.ldexp(10,2) =>",math.ldexp(10,2)) #* 1.parametreyi 2 üzeri 2.parametre ile çarpar
print("math.log(16,2) =>",math.log(16,2)) #* 1.parametrenin doğal logaritmasını alır
print("math.log10(100) =>",math.log10(100)) #* 1.parametrenin 10 tabanında logaritmasını alır
print("math.log1p(100) =>",math.log1p(100)) #* 1.parametrenin 1 fazlasının doğal logaritmasını alır
print("math.log2(100) =>",math.log2(100)) #* 1.parametrenin 2 tabanında logaritmasını alır
print("math.perm(10,5) =>",math.perm(10,5)) #* 1.parametrenin 2.parametreye göre permütasyonunu alır
print("math.pow(10,2) =>",math.pow(10,2)) #* 1.parametrenin 2.parametreye göre kuvvetini alır
print("math.modf(10.5) =>",math.modf(10.5)) #* 1.parametrenin ondalıklı ve tam kısmını verir


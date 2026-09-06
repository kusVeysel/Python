from datetime import datetime as dt
from datetime import timezone as tz
import locale as lcl
from datetime import timedelta as td
from datetime import date, time
import time as tm

print("dt.now()=>",dt.now()) #* şuanın tarih ve saatini alır
print("dt.now().hour =>",dt.now().hour) #* şuanın sadece saat kısmını verir
print("dt.now().minute =>",dt.now().minute) #* şuanın sadece dakika kısmını verir
print("dt.now().second =>",dt.now().second) #* şuanın sadece saniye kısmını verir
print("dt.now().microsecond =>",dt.now().microsecond) #* şuanın sadece mikrpsaniye kısmını verir
print("dt.weekday(dt.now()) =>",dt.weekday(dt.now())) #* haftanın kaçıncı gününde olduğunu verir, index mantığına göre verir(yani pazar için 6 döner)
print("dt.ctime(dt.now()) =>",dt.ctime(dt.now())) #* detaylı tarih verir


#? strftime metotu
print()
print("dt.now().strftime(\"%a\") =>",dt.now().strftime("%a")) #* haftanın gününün kısaltmasını verir
print("dt.now().strftime(\"%A\") =>",dt.now().strftime("%A")) #* haftanın gününün uzun halini verir
print("dt.now().strftime(\"%w\") =>",dt.now().strftime("%w")) #* haftanın kaçıncı günü olduğunu verir
print("dt.now().strftime(\"%d\") =>",dt.now().strftime("%d")) #* ayın kaçıncı günü olduğunu verir
print("dt.now().strftime(\"%b\") =>",dt.now().strftime("%b")) #* ayın kısaltmasını verir
print("dt.now().strftime(\"%B\") =>",dt.now().strftime("%B")) #* ayın uzun halini verir
print("dt.now().strftime(\"%m\") =>",dt.now().strftime("%m")) #* kaçıncı ayda olduğumuzu verir
print("dt.now().strftime(\"%y\") =>",dt.now().strftime("%y")) #* kaçıncı yılda olduğumuzun son iki rakamını verir
print("dt.now().strftime(\"%Y\") =>",dt.now().strftime("%Y")) #* kaçıncı yılda olduğumuzu verir
print("dt.now().strftime(\"%H\") =>",dt.now().strftime("%H")) #* 24lük saaate göre saati verir
print("dt.now().strftime(\"%I\") =>",dt.now().strftime("%I")) #* 12lik saaate göre saati verir
print("dt.now().strftime(\"%p\") =>",dt.now().strftime("%p")) #* PM
print("dt.now().strftime(\"%M\") =>",dt.now().strftime("%M")) #* dakikayı verir
print("dt.now().strftime(\"%S\") =>",dt.now().strftime("%S")) #* saniyeyi verir
print("dt.now().strftime(\"%f\") =>",dt.now().strftime("%f")) #* mikrosaniyeyi verir
print("dt.now().strftime(\"%G\") =>",dt.now().strftime("%G")) #* iso yılına göre yılı verir
print("dt.now().strftime(\"%u\") =>",dt.now().strftime("%u")) #* iso 8601'e göre haftanın kaçıncı günü olduğuunu gösterir
print("dt.now().strftime(\"%V\") =>",dt.now().strftime("%V")) #* iso 8601'e göre yılın kaçıncı haftası olduğuunu gösterir

#? timezome sınıfı
print()
Tz = dt.now(tz.utc)
print("Tz.strftime(\"%z\") =>",Tz.strftime("%z")) #* zaman dilimini verir
print("Tz.strftime(\"%Z\") =>",Tz.strftime("%Z")) #* UTC
print("Tz.strftime(\"%j\") =>",Tz.strftime("%j")) #* yılın kaçıncı gününde olduğunu verir 
print("Tz.strftime(\"%U\") =>",Tz.strftime("%U")) #* yılın kaçıncı haftada olduğunu verir (saymaya pazardan başlar)
print("Tz.strftime(\"%W\") =>",Tz.strftime("%W")) #* yılın kaçıncı haftada olduğunu verir (saymaya pazartesinden başlar)

#? locale module
# lcl.setlocale(lcl.LC_TIME,"x") x => ülke ayarı

lcl.setlocale(lcl.LC_TIME,"tr-TR.UTF-8")
my_locale = dt.now()
print("my_locale.strftime(\"%c\") =>",my_locale.strftime("%c")) #* ülkeye göre tarih ve saat yazar
print("my_locale.strftime(\"%C\") =>",my_locale.strftime("%C")) #* yılın ilk iki rakamını verir
lcl.setlocale(lcl.LC_TIME,"en-US.UTF-8")
print("my_locale.strftime(\"%c\") =>",my_locale.strftime("%c")) #* ülkeye göre tarih ve saat yazar
print("my_locale.strftime(\"%x\") =>",my_locale.strftime("%x")) #*ülkeye göre tarihi verir
print("my_locale.strftime(\"%X\") =>",my_locale.strftime("%X")) #*ülkeye göre zamanı verir
print("my_locale.strftime(\"%%\") =>",my_locale.strftime("%%")) #* % işaretini verir

#?
print()
text = "11 August 2026 hour 21:42:00"
dttime = dt.strptime(text,"%d %B %Y hour %H:%M:%S")
print(dttime)
#* stringi datetime çevirir

print(dt.timestamp(dt.now())) #* 1970'den şuana kadar geçen zamanı verir

#? timedelta sınıfı
#* zamanı ileri geri almaya yarar
print()

date1 = dt(2026,1,15)
date2 = dt(2026,1,8)

difference = date1-date2
print(difference)
print(difference.days)

today =dt.now()
new_today = today+td(days=7)
print(new_today)
new_today2 = today-td(days=5)
print(new_today2)

#? 
print()
my_date = date(2026,8,11)
my_time = time(21,58,00)
print(dt.combine(my_date,my_time)) #* tarih ve saati birleştirir
print(today.replace(hour=7,minute=19)) #* update gibi günceller yer değiştirir
tm.sleep(3) #* 3 saniye uyutur

start = tm.process_time()
for _ in range(1000000):
    ...

end = tm.process_time()

print(end-start) #* işlem için işlemcide harcanan süreyi verir
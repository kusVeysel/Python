 #? DateTime Module

#* datetime modülü tarih, saat, zaman farkı ve zaman dilimi işlemlerini yapar.

from datetime import date, datetime, time, timedelta, timezone
import time as time_module

#? Anlık tarih ve saat
print("-----Anlık Tarih ve Saat-----")
now = datetime.now()
print(f"datetime.now() → {now}") #* bilgisayarın yerel tarih ve saatini verir
print(f"now.date() → {now.date()}") #* datetime nesnesinden yalnızca tarihi alır
print(f"now.time() → {now.time()}") #* datetime nesnesinden yalnızca saati alır
print(f"now.year → {now.year}") #* yılı verir
print(f"now.month → {now.month}") #* ayı verir
print(f"now.day → {now.day}") #* ayın gününü verir
print(f"now.hour → {now.hour}") #* saati verir
print(f"now.minute → {now.minute}") #* dakikayı verir
print(f"now.second → {now.second}") #* saniyeyi verir
print(f"now.weekday() → {now.weekday()}") #* pazartesi 0, pazar 6 olacak şekilde günü verir
print(f"now.isoweekday() → {now.isoweekday()}") #* pazartesi 1, pazar 7 olacak şekilde günü verir
print(f"now.ctime() → {now.ctime()}") #* tarihi okunabilir metin biçiminde verir
print("------------------------------------------")

#? Tarihi biçimlendirme
print("-----strftime ve strptime-----")
print(f"now.strftime('%d/%m/%Y') → {now.strftime('%d/%m/%Y')}") #* tarihi metne çevirir
print(f"now.strftime('%H:%M:%S') → {now.strftime('%H:%M:%S')}") #* saati biçimlendirilmiş metin olarak verir
text = "11 August 2026 21:42:00"
parsed_date = datetime.strptime(text, "%d %B %Y %H:%M:%S") #* metni datetime nesnesine çevirir
print(f"datetime.strptime(text, format) → {parsed_date}")
print("------------------------------------------")

#? Tarih, saat ve zaman farkı
print("-----date, time ve timedelta-----")
my_date = date(2026, 8, 11)
my_time = time(21, 58, 0)
print(f"date(2026, 8, 11) → {my_date}") #* tarih nesnesi oluşturur
print(f"time(21, 58, 0) → {my_time}") #* saat nesnesi oluşturur
print(f"datetime.combine(my_date, my_time) → {datetime.combine(my_date, my_time)}") #* tarih ve saati birleştirir
date1 = datetime(2026, 1, 15)
date2 = datetime(2026, 1, 8)
difference = date1 - date2
print(f"date1 - date2 → {difference}") #* iki tarih arasındaki zaman farkını verir
print(f"difference.days → {difference.days}") #* zaman farkının gün kısmını verir
print(f"now + timedelta(days=7) → {now + timedelta(days=7)}") #* tarihe 7 gün ekler
print(f"now - timedelta(days=5) → {now - timedelta(days=5)}") #* tarihten 5 gün çıkarır
print(f"now.replace(hour=7, minute=19) → {now.replace(hour=7, minute=19)}") #* belirtilen tarih-saat alanlarını değiştirir
print("------------------------------------------")

#? Zaman dilimi ve timestamp
print("-----Zaman Dilimi ve Timestamp-----")
utc_now = datetime.now(timezone.utc)
print(f"datetime.now(timezone.utc) → {utc_now}") #* UTC zaman dilimindeki tarih ve saati verir
print(f"utc_now.tzname() → {utc_now.tzname()}") #* zaman diliminin adını verir
print(f"utc_now.strftime('%z') → {utc_now.strftime('%z')}") #* UTC farkını +0000 biçiminde verir
print(f"datetime.timestamp(now) → {datetime.timestamp(now)}") #* 1970 başlangıcından beri geçen saniyeyi verir
print(f"datetime.fromtimestamp(datetime.timestamp(now)) → {datetime.fromtimestamp(datetime.timestamp(now))}") #* timestamp değerini datetime nesnesine çevirir
print("------------------------------------------")

#? Performans ölçümü
print("-----time Modülü-----")
start = time_module.perf_counter()
for _ in range(100000):
    pass
elapsed = time_module.perf_counter() - start
print(f"time.perf_counter() ile geçen süre → {elapsed}") #* yüksek hassasiyetle geçen gerçek süreyi ölçer
print("------------------------------------------")

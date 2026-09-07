 #? DateTime Module

#* datetime modülü tarih, saat, zaman farkı ve zaman dilimi işlemlerini yapar.

from datetime import date, datetime, time, timedelta, timezone
import time as time_module

#? Anlık tarih ve saat
print("-----Anlık Tarih ve Saat-----")
now = datetime.now()
print(f"datetime.now() → {now}")
print(f"now.date() → {now.date()}")
print(f"now.time() → {now.time()}")
print(f"now.year → {now.year}")
print(f"now.month → {now.month}")
print(f"now.day → {now.day}")
print(f"now.hour → {now.hour}")
print(f"now.minute → {now.minute}")
print(f"now.second → {now.second}")
print(f"now.weekday() → {now.weekday()}") #* pazartesi 0, pazar 6 olacak şekilde günü verir
print(f"now.isoweekday() → {now.isoweekday()}") #* pazartesi 1, pazar 7 olacak şekilde günü verir
print(f"now.ctime() → {now.ctime()}")
print("------------------------------------------")

#? Tarihi biçimlendirme
print("-----strftime ve strptime-----")
print(f"now.strftime('%d/%m/%Y') → {now.strftime('%d/%m/%Y')}") #* tarihi metne çevirir
print(f"now.strftime('%H:%M:%S') → {now.strftime('%H:%M:%S')}")
text = "11 August 2026 21:42:00"
parsed_date = datetime.strptime(text, "%d %B %Y %H:%M:%S") #* metni datetime nesnesine çevirir
print(f"datetime.strptime(text, format) → {parsed_date}")
print("------------------------------------------")

#? Tarih, saat ve zaman farkı
print("-----date, time ve timedelta-----")
my_date = date(2026, 8, 11)
my_time = time(21, 58, 0)
print(f"date(2026, 8, 11) → {my_date}")
print(f"time(21, 58, 0) → {my_time}")
print(f"datetime.combine(my_date, my_time) → {datetime.combine(my_date, my_time)}")
date1 = datetime(2026, 1, 15)
date2 = datetime(2026, 1, 8)
difference = date1 - date2
print(f"date1 - date2 → {difference}")
print(f"difference.days → {difference.days}")
print(f"now + timedelta(days=7) → {now + timedelta(days=7)}")
print(f"now - timedelta(days=5) → {now - timedelta(days=5)}")
print(f"now.replace(hour=7, minute=19) → {now.replace(hour=7, minute=19)}")
print("------------------------------------------")

#? Zaman dilimi ve timestamp
print("-----Zaman Dilimi ve Timestamp-----")
utc_now = datetime.now(timezone.utc)
print(f"datetime.now(timezone.utc) → {utc_now}")
print(f"utc_now.tzname() → {utc_now.tzname()}")
print(f"utc_now.strftime('%z') → {utc_now.strftime('%z')}")
print(f"datetime.timestamp(now) → {datetime.timestamp(now)}") #* 1970 başlangıcından beri geçen saniyeyi verir
print(f"datetime.fromtimestamp(datetime.timestamp(now)) → {datetime.fromtimestamp(datetime.timestamp(now))}")
print("------------------------------------------")

#? Performans ölçümü
print("-----time Modülü-----")
start = time_module.perf_counter()
for _ in range(100000):
    pass
elapsed = time_module.perf_counter() - start
print(f"time.perf_counter() ile geçen süre → {elapsed}") #* geçen gerçek süreyi ölçer
print("------------------------------------------")

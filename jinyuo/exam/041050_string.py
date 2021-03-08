# https://wikidocs.net/78558

print("041")
ticker = "btc_krw"
print(ticker.upper())

print("\n042")
ticker = "BTC_KRW"
print(ticker.lower())

print("\n043")
print("hello".capitalize())

print("\n044")
file_name = "2020_보고서.xlsx"
print(file_name.endswith("xlsx"))

print("\n045")
print(file_name.endswith(("xlsx" , "xls")))

print("\n046")
print(file_name.startswith("2020"))

print("\n047")
a = "hello world"
print(a.split(" "))

print("\n048")
ticker = "btc_krw"
print(ticker.split("_"))

print("\n049")
date = "2020-05-01"
print(date.split("-"))

print("\n050")
data = "039490     "
print(data.rstrip())

def binary(s):
    year ,month , date = s.split("-")
    return f'{int(year):b}-{int(month):b}-{int(date):b}'

s = "2004-10-09"

print(binary(s))
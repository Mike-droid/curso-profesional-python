from datetime import datetime

my_datetime = datetime.now()
print(my_datetime)

latam = my_datetime.strftime('%d/%m/%Y')
print(f'Formato LATAM: {latam}')

usa = my_datetime.strftime('%m/%d/%Y')
print(f'Formato USA: {usa}')

random_format = my_datetime.strftime('año %Y mes %m día %d')
print(f'Formato random: {random_format}')

formato_utc = datetime.utcnow()
print(f'Formato UTC: {formato_utc}')
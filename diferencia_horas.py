from datetime import datetime
import pytz

def get_date_time_from_timezone(city_name:str, timezone:str)-> datetime:
  city_timezone = pytz.timezone(timezone)
  return datetime.now(city_timezone)


london = get_date_time_from_timezone("London", "Europe/London")
cdmx = get_date_time_from_timezone("LA", "America/Los_Angeles")


difference = london - cdmx
print(f'Diferencia entre London y CDMX: {difference}')
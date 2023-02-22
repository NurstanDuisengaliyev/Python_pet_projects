import datetime

#Write a Python program to subtract five days from current date.

print(datetime.date.today() - datetime.timedelta(days=5))

#Write a Python program to print yesterday, today, tomorrow.
print(f"Tomorrow was {datetime.date.today() - datetime.timedelta(days=1)}")
print(f"Tomorrow was {datetime.date.today() - datetime.timedelta(days=0)}")
print(f"Tomorrow was {datetime.date.today() - datetime.timedelta(days=-1)}")

#Write a Python program to drop microseconds from datetime.

print(datetime.datetime.today().replace(microsecond=0))

#Write a Python program to calculate two date difference in seconds.

date1 = datetime.date.today()
date2 = datetime.date.fromisoformat('2023-03-04')

print((date2 - date1).total_seconds())
from datetime import datetime,timedelta

now=datetime.now()
print(now)

yesterday=now-timedelta(days=1)
print(yesterday)
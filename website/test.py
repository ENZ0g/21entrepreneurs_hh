from datetime import datetime, timedelta


t = datetime.now().date()
print(t)
print(t + timedelta(days=10))
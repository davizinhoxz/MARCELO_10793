from datetime import datetime

data = datetime.now()
data = data.strftime("%d-%m-%Y %H:%M:%S")
print(data)
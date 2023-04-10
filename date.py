from datetime import datetime
#from datetime import date
#from datetime import time

#import datetime

simdi = datetime.now()
simdi = datetime.today()

result = simdi
result = simdi.year
result = simdi.month
result = simdi.day
result = simdi.hour
result = simdi.minute
result = simdi.second

result = datetime.ctime(simdi)
result = datetime.strftime(simdi,"%Y")


print(result)


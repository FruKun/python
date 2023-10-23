from datetime import date, timedelta
def generate_date(year, month, day, count):
    n=0
    a=date(year,month,day)
    while(n<count):
        yield a+timedelta(days=n)
        n+=1

def generate_dow(year, month, day,count):
    weekDays = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    a= date(year,month,day)
    b=a
    n=0
    while(n<count):
        yield weekDays[a.weekday()]
        a+=timedelta(days=1)
        n+=1
my_dates=generate_date(2000,10,10, 100)
weeks = generate_dow(2000,10,10, 100)
list = []
n=0
while(n<100):
    a = next(my_dates).isoformat()
    b = next(weeks)
    list.append(a + " " + b)
    n+=1
for i in list:
    print(i)



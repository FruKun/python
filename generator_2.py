from datetime import date, timedelta
def generate_date(year, month, day, count):
    n=0
    a=date(year,month,day)
    while(n<count):
        yield a+timedelta(days=n)
        n+=1
my_dates=generate_date(2000,10,10,100)
for i in my_dates:
    print(i)


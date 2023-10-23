from datetime import date,timedelta
def generate_dow(year, month, day,count):
    weekDays = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    a= date(year,month,day)
    b=a
    n=0
    while(n<count):
        yield weekDays[a.weekday()]
        a+=timedelta(days=1)
        n+=1

for i in generate_dow(2020,10,21, 3):
    print(i)
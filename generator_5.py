def abba(a):
    for i in a:
        yield i

with open("abba.txt") as file:
    a = file.readlines()
    b = abba(a)
    for i in range(5):
        print(next(b).rstrip())

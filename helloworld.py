import math
f = open("1.txt", "r")
a = f.read()
f.close()
f = open("2.txt", "r")
a1 = f.read()
f.close()
text1 = a.split()
text2 = a1.split()
ltext1 = len(text1)
ltext2 = len(text2)
wtext1 = text1.count("abba")
wtext2 = text2.count("abba")
fcount = 0
if wtext1 >0:
    fcount+=1
if wtext2 >0:
    fcount +=1
tf = wtext1 / ltext1
idf = math.log(fcount/2, 100)
tf_idf = tf * idf
print(tf_idf)
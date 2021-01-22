m = int(input())
t = int((m - (m % 10)) / 10)
f = 0
o = 0
m = m - (t * 10)
if m == 0:
    o = 0
    f = 0
elif m == 5:
    o = 0
    f = 1
elif m > 5:
    o = m - 5
    f = 1
elif m < 5:
    o = m
    f = 0
print(o + f + t)

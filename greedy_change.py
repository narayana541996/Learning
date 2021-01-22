m = int(input())###Not working for all cases, didn't try fixing.
                #check the non_loop_change.py for a more efficient solution.
t = 0
f = 0
o = 0
while t * 10 + f * 5 + o < m:
    if t * 10 < m - (m % 10):
        t += 1
    if t * 10 == m - (m % 10):
        if (m % 10) > 5 and (f * 5) < (m - (t * 10)):
            f += 1
    if t * 10 == m - (m % 10):
        if m - (t * 10) - (f * 5) < 5 and  m - (t * 10) - (f * 5) > 0:
            o += 1
    #print(o,' ',f,' ',t)
print(o + f + t)

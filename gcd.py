a, b = map(int, input().split())
if b < a:
    temp = a
    a = b
    b = temp
r = b % a
while r > 0:
    if r < a:
        b = a
        a = r
        r = b % a
    else:
        break
if r == 0:
    print(a)
if r != 0:
    print(1)

a, b = map(int, input().split())
if b < a:
    temp = b
    b = a
    a = temp
i = 1
while i <= b:
    
    if not (a * i) % b:
        print(a * i)
        break
    i += 1
if i > b:
    print(a * b)

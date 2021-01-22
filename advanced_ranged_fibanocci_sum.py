m, n = map(int, input().split())
def fib_sum(n):
    n = n + 2
    i = 3
    m2 = 10
#series = [0, 1]
    sum1 = 1
    sum2 = 2
    reminders = [0, 1 % m2, 1 % m2]
    if n - 2 == 0:
    #print(0)
    #exit()
        return 0
    elif n - 2 == 1:
    #print(1)
    #exit()
        return 1
    if n <= len(reminders):
    #print(reminders[n])
        return reminders[n]
    else:
        while True:
            if reminders[i - 2]  == 0:
                if reminders[i - 1]  == 1:
                    break
            reminders.append(sum2 % m2)
            temp = sum2
            sum2 = sum1 + sum2
            sum1 = temp
            i += 1
        reminders.pop()
        reminders.pop()
        if reminders[n % len(reminders)]:
            print(reminders)
            print('n: ',n,' ',(reminders[n % len(reminders)] - 1))
            return (reminders[n % len(reminders)] - 1) 
        else:
            #print(9)
            return 9


#else:
if m == 0 and n == 0:
    print(0)
    exit()
if m == 0 and n == 1:
    print(1)
    exit()
if n == 0 and n >= m:
    print(0)
    exit()
if m == 0:
    print(fib_sum(n))
    exit()
elif n == 0:
    print(fib_sum(m))
    exit()
if m < n:
    a = fib_sum(n)
    b = fib_sum(m - 1)
    print(a,'a b',b)
else:
    a = fib_sum(n - 1)
    b = fib_sum(m)
    print(a,'a b ',b)
if n > 1 and a < 5:
    a = 10 + a
    print(a,'a b ',b)
if m > 1 and b < 5:
    b = 10 + b
    print(a,'a b ',b)
print(abs(a - b) % 10)
    #if m > n:
     #   print(abs(fib_sum(m) - fib_sum(n - 1)))

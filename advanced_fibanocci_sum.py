m, n = map(int, input().split())
n = n + 2
i = 3
#series = [0, 1]
sum1 = 1
sum2 = 2
reminders = [0, 1 % m, 1 % m]
if n - 2 == 0:
    print(0)
    exit()
elif n - 2 == 1:
    print(1)
    exit()
if n <= len(reminders):
    print(reminders[n])
else:
    while True:
        if reminders[i - 2]  == 0:
            if reminders[i - 1]  == 1:
                break
        reminders.append(sum2 % m)
        temp = sum2
        sum2 = sum1 + sum2
        sum1 = temp
        i += 1
    reminders.pop()
    reminders.pop()
    if reminders[n % len(reminders)]:
        print(reminders[n % len(reminders)] - 1)
    else:
        print(9)

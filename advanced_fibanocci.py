n, m = map(int, input().split())
i = 3
#series = [0, 1]
sum1 = 1
sum2 = 2
reminders = [0, 1 % m, 1 % m]
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
    print(reminders[n % len(reminders)])

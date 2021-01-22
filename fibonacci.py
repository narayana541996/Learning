n = int(input())

if n == 0:
    print(0)
elif n == 1:
    print(1)

else:
    i = 2
    series = [0, 1]
    while i <= n:
        series.append(series[i - 1] + series[i - 2])
        i += 1
    print(series[-1])

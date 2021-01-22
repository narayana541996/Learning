n = int(input())
series = [0, 1]
i = 2
while i <= n:
    series.append(int(str(series[i - 1] + series[i - 2])[-1]))
    i += 1
print(series[-1])

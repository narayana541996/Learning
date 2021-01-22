n = int(input())
series = [0, 1]
i = 2
while i <= n:
    series.append((series[i - 1] + series[i - 2])%10)
    i += 1
print(series[-1])

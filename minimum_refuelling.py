d = int(input())
m = int(input())
if m >= d:
    print(0)
    exit()
n = int(input())
stops = list(map(int, input().split()))
if stops[0] > m or abs(stops[-1] - d) > m:
    print(-1)
    exit()
for i in range(n - 1):
    if stops[i + 1] - stops[i] > m:
        print(-1)
        exit()
#if d % m == 0:
print(int(d/m))
#else:
 #   print(d/m + 1)

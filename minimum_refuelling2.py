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

print('stops: ', stops)
for i in range(n - 1):
    if abs(stops[i + 1] - stops[i]) > m:
        print(-1)
        exit()
#####try a test with L=1 where the answer is not -1
#####try sorting the list.
#####check if there are equal elements.
        
print('stops2: ', stops)
cur = 0
nxt = stops[0]
i = 1
steps = 0
pre = 0
while cur <= d:
    if abs(nxt - cur) == m:
        pre = cur
        cur = nxt
        steps += 1
        continue
    elif abs(nxt - cur) > m:
        cur = pre
        steps += 1
        continue
    if nxt == d:
        break
    if i < n:
        #print(stops[i])
        nxt = stops[i]
    else:
        nxt = d
    i += 1
    if i > 2:
        pre = stops[i - 2]
    #print('pre: ',pre)
print(steps)

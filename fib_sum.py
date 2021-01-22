##Slow solution
n = int(input())
pre_num = 0
post_num = 1
if n > 0:
    nsum = 1
else:
    nsum = 0
i = 2
while i <= n:
    temp = post_num % 10
    post_num = pre_num + post_num
    pre_num = temp
    nsum = nsum + post_num
    i += 1
print(nsum)

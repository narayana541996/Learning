def sort(seq):
    sorted_seq = []
    while len(seq):
        max_ = seq[-1]
        for item in seq:
            #print('sorted_seq: ',sorted_seq,' max_: ', max_,' seq: ', seq)
            
            if item > max_:
                max_ = item
        sorted_seq.append(seq.pop(seq.index(max_)))
        if len(seq) == 1:
            sorted_seq.append(seq.pop(0))

    return sorted_seq

n = int(input())
ppc = sort(list(map(int, input().split())))
avg_clicks = sort(list(map(int, input().split())))
#print(ppc,' ',avg_clicks)
sum_ = 0
for i in range(n):
    sum_ = sum_ + (ppc[i] * avg_clicks[i])
print(sum_)

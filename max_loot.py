n, tw = map(int, input().split())
v = [0 for i in range(n)]
w = [0 for i in range(n)]
v_w = [0 for i in range(n)]
tv = 0
w_sum = 0
for i in range(n):
    v[i], w[i] = map(int, input().split())
    #print(v,' ', w)
    v_w[i] = v[i]/w[i]
#print(v,' ',w,' ',v_w)
maximum = v_w[0]
for item in w:
    w_sum += item
if w_sum > tw:
    while tw:
        for value in v_w:
            if maximum < value:
                maximum = value
        chosen_index = v_w.index(maximum)
        chosen_v = v[chosen_index]
        chosen_w = w[chosen_index]    
        if chosen_w <= tw:
            tw -= chosen_w
            tv += chosen_v
            w.pop(chosen_index)
            v.pop(chosen_index)
            v_w.pop(chosen_index)
            maximum = v_w[0]
        else:
            tv += (tw/chosen_w)*chosen_v
            tw = 0
            break
else:
    for value in v:
        tv += value
print(tv)

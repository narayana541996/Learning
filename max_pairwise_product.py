n = int(input())
numbers = []
for number in map(int, input().split()):
    numbers.append(number)
max2 = [numbers[0], numbers[1]]
for number in numbers[2:]:
    if number > max2[0]:
        if max2[0] > max2[1]:
            max2[1] = max2[0]
        max2[0] = number
    elif number > max2[1]:
        max2[1] = number
print(max2[0] * max2[1])

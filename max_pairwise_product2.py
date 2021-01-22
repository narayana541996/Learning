n = int(input())
numbers = []
for num in map(int, input().split()):
    numbers.append(num)
i = 0
while i < (n - 1):
    if numbers[i] > numbers[i+1]:
        temp = numbers[i+1]
        numbers[i + 1] = numbers[i]
        numbers[i] = temp
    j = i
    while j > 0:
        if numbers[j - 1] > numbers[j]:
            temp = numbers[j]
            numbers[j - 1] = numbers[j]
            numbers[j] = temp
        j -= 1
    i += 1

print(numbers[-1] * numbers[-2])

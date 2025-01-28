def scuare_sum(numbers):
    sum = 0

    for num in numbers:
        sum = sum + (num * num)

    return sum

print(scuare_sum({1,2,2}))
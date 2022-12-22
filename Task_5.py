import random

def shaffle_list(row: list):
    for i in range(len(row)):
        row.insert(random.randint(0, len(row) - 1), row.pop(i))
    return row

sorted = list(range(10, 51))
print(*sorted)
unsorted = shaffle_list(sorted.copy())
print(*unsorted)
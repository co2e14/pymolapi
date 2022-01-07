import csv

with open('all.txt', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

data = data[0]
print(len(data))

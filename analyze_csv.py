
import csv

threshold = 70
with open('students.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        grades = list(map(int, row['grade'].split(',')))
        avg = sum(grades) / len(grades)
        if avg > threshold:
            print(row['name'])

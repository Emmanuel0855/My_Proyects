import csv

def import_csv(filename):
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]  # Convertimos el generador en una lista
    return data

students_data = import_csv('students_data1.csv')
print(students_data)
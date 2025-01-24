# Exercise 6: Vector of 10 integers
def fill_vector():
    vector = []
    print("Enter numbers to fill the vector (up to 10 elements). Enter a negative number to stop.")
   
    while len(vector) < 10:
        num = int(input(f"Enter number {len(vector) + 1}: "))
        if num < 0:
            break
        vector.append(num)
   
    print("Filled vector:", vector)

# Exercise 7: Names and ages of students
def students_data():
    students = []
   
    while True:
        name = input("Enter the student's name (or type 'stop' to finish): ")
        if name.lower() == 'stop':
            break
        age = int(input(f"Enter {name}'s age: "))
        students.append({"name": name, "age": age})
   
    print("\nStudents over 21 years old:")
    for student in students:
        if student['age'] > 21:
            print(student['name'])
   
    oldest_age = max(student['age'] for student in students)
    print("\nOldest student(s):")
    for student in students:
        if student['age'] == oldest_age:
            print(student['name'])
def main():
    # Task 6: Fill vector with numbers until vector is full or a negative number is entered
    fill_vector()

    # Task 7: Collect student information and display results
    students_data()


if __name__ == "__main__":
    main()
import random

# Exercise 1: Initialize vector with random integers and show square and cube
def exercise_1():
    vector_numeros = [random.randint(1, 10) for _ in range(10)]
    
    print("Exercise 1: Numbers, their squares, and cubes")
    for num in vector_numeros:
        square = num ** 2
        cube = num ** 3
        print(f'Number: {num}, Square: {square}, Cube: {cube}')
    print()  # Line break for better output formatting

# Exercise 2: Read 5 notes and show all, middle, highest, and lowest
def exercise_2():
    notes = []
    for i in range(5):
        note = float(input(f'Enter note {i+1} (between 0 and 10): '))
        notes.append(note)
    
    print("Exercise 2: Notes summary")
    print("All notes:", notes)
    middle_note = sum(notes) / len(notes)
    print("Middle note:", middle_note)
    highest_note = max(notes)
    lowest_note = min(notes)
    print("Highest note:", highest_note)
    print("Lowest note:", lowest_note)
    print()

# Exercise 3: Read 5 strings, reverse them, and display both original and reversed vectors
def exercise_3():
    original_vector = [input(f'Enter string {i+1}: ') for i in range(5)]
    reversed_vector = original_vector[::-1]
    
    print("Exercise 3: Original and reversed strings")
    print("Original vector:", original_vector)
    print("Reversed vector:", reversed_vector)
    print()

# Exercise 4: Ask for a month number and display month name and days
def exercise_4():
    months = [
        ("January", 31), ("February", 28), ("March", 31),
        ("April", 30), ("May", 31), ("June", 30),
        ("July", 31), ("August", 31), ("September", 30),
        ("October", 31), ("November", 30), ("December", 31)
    ]

    month_num = int(input("Enter the number of the month (1-12): "))
    if 1 <= month_num <= 12:
        month_name, days = months[month_num - 1]
        print(f'Month: {month_name}, Days: {days}')
    else:
        print("Invalid month number. Please enter a number between 1 and 12.")
    print()

# Exercise 5: Initialize a vector with random numbers and sort it
def exercise_5():
    vector = [random.randint(1, 100) for _ in range(10)]
    
    print("Exercise 5: Sorting random numbers")
    print("Original vector:", vector)
    sorted_vector = sorted(vector)
    print("Sorted vector:", sorted_vector)
    print()

# Main function to run all exercises
def run_all_exercises():
    exercise_1()
    exercise_2()
    exercise_3()
    exercise_4()
    exercise_5()

# Run all exercises
run_all_exercises()
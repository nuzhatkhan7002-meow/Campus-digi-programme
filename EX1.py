# =========================================================
# SMART CAMPUS DIGITALIZATION SYSTEM
# Mini Project Integration using Python
# =========================================================

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# =========================================================
# MODULE 1
# Student Registration and Grade Evaluation
# =========================================================

def student_registration():

    print("\n===== STUDENT REGISTRATION =====")

    student_name = input("Enter student name: ")
    score = float(input("Enter exam score (0-100): "))

    if score >= 90 and score <= 100:
        grade = "A"
        remark = "Excellent"

    elif score >= 75:
        grade = "B"
        remark = "Very Good"

    elif score >= 60:
        grade = "C"
        remark = "Good"

    elif score >= 40:
        grade = "D"
        remark = "Average"

    else:
        grade = "F"
        remark = "Needs Improvement"

    print("\n--- Student Report ---")
    print("Name:", student_name)
    print("Score:", score)
    print("Grade:", grade)
    print("Performance Remark:", remark)


# =========================================================
# MODULE 2
# Course Enrollment Management
# =========================================================

def course_enrollment():

    print("\n===== COURSE ENROLLMENT =====")

    courses = []
    max_courses = 5

    while True:

        if len(courses) >= max_courses:
            print("Maximum course limit reached!")
            break

        course_name = input("Enter course name (or 'done' to finish): ")

        if course_name.lower() == "done":
            break

        credits = input("Enter credit value: ")

        if not credits.isdigit():
            print("Invalid credit value! Skipping entry...")
            continue

        credits = int(credits)

        if credits <= 0:
            print("Credit must be positive! Skipping entry...")
            continue

        courses.append((course_name, credits))

        print(f"Course '{course_name}' added successfully.\n")

    print("\n--- Enrollment Report ---")

    for course, credit in courses:
        print("Course:", course, "| Credits:", credit)

    print("Total courses enrolled:", len(courses))


# =========================================================
# MODULE 3
# Student Record Management using Data Structures
# =========================================================

def student_records():

    print("\n===== STUDENT RECORD MANAGEMENT =====")

    students = []

    n = int(input("How many student records to add? "))

    for i in range(n):

        print(f"\nEnter details for Student {i+1}")

        name = input("Enter Name: ")
        age = int(input("Enter Age: "))

        grades = []

        for j in range(3):
            mark = int(input(f"Enter Grade {j+1}: "))
            grades.append(mark)

        students.append({
            "name": name,
            "age": age,
            "grades": grades
        })

    print("\n=== Student Records ===")

    for student in students:

        print("-----------------------")
        print("Name:", student["name"])
        print("Age:", student["age"])
        print("Grades:", student["grades"])

    # Sets Example

    event_A = {"Priya", "Rahul", "Anita", "Kiran"}
    event_B = {"Rahul", "Anita", "Sneha"}

    common_participants = event_A & event_B
    all_participants = event_A | event_B
    only_event_A = event_A - event_B

    print("\n=== Event Participation Analysis ===")
    print("Common Participants:", common_participants)
    print("All Participants:", all_participants)
    print("Only Event A Participants:", only_event_A)


# =========================================================
# MODULE 4
# Sorting and Searching Student IDs
# =========================================================

def sorting_searching():

    print("\n===== SORTING AND SEARCHING =====")

    student_ids = [105, 102, 110, 108, 101, 115]

    print("Original IDs:", student_ids)

    # Bubble Sort

    n = len(student_ids)

    for i in range(n):

        for j in range(0, n-i-1):

            if student_ids[j] > student_ids[j+1]:

                temp = student_ids[j]
                student_ids[j] = student_ids[j+1]
                student_ids[j+1] = temp

    print("Sorted IDs:", student_ids)

    # Linear Search

    target = int(input("Enter Student ID to search: "))

    found = False

    for i in range(len(student_ids)):

        if student_ids[i] == target:

            print("Linear Search: ID found at index", i)
            found = True
            break

    if not found:
        print("Linear Search: ID not found")

    # Binary Search

    low = 0
    high = len(student_ids) - 1
    found_index = -1

    while low <= high:

        mid = (low + high) // 2

        if student_ids[mid] == target:

            found_index = mid
            break

        elif student_ids[mid] < target:

            low = mid + 1

        else:

            high = mid - 1

    if found_index != -1:
        print("Binary Search: ID found at index", found_index)

    else:
        print("Binary Search: ID not found")


# =========================================================
# MODULE 5
# Fee Calculation using Functions
# =========================================================

def calculate_fee(tuition_fee, hostel_fee=0, transport_fee=0):

    total_fee = tuition_fee + hostel_fee + transport_fee

    return total_fee


def fee_management():

    print("\n===== STUDENT FEE CALCULATION =====")

    tuition = int(input("Enter Tuition Fee: "))
    hostel = int(input("Enter Hostel Fee: "))
    transport = int(input("Enter Transport Fee: "))

    total = calculate_fee(tuition, hostel, transport)

    print("Total Fee:", total)


# =========================================================
# MODULE 6
# File Handling for Student Academic Records
# =========================================================

def file_handling():

    print("\n===== FILE HANDLING =====")

    with open("student_records.txt", "w") as file:

        file.write("ID,Name,Marks\n")
        file.write("101,Nate,85\n")
        file.write("102,Jules,92\n")
        file.write("103,Maddie,76\n")
        file.write("104,Cassie,89\n")

    print("Student records written successfully.")

    print("\nReading Student Records:\n")

    with open("student_records.txt", "r") as file:

        records = file.readlines()

        for record in records:
            print(record.strip())

    total_students = 0
    total_marks = 0
    highest_marks = -1
    top_student = ""

    for record in records[1:]:

        parts = record.strip().split(",")

        name = parts[1]
        marks = int(parts[2])

        total_students += 1
        total_marks += marks

        if marks > highest_marks:

            highest_marks = marks
            top_student = name

    average_marks = total_marks / total_students

    print("\n===== REPORT =====")
    print("Total Students:", total_students)
    print("Average Marks:", average_marks)
    print("Top Student:", top_student)
    print("Highest Marks:", highest_marks)


# =========================================================
# MODULE 7
# Directory Scanning with Exception Handling
# =========================================================

class MissingFileOrFolderError(Exception):

    pass


def scan_directory(path):

    try:

        if not os.path.exists(path):
            raise FileNotFoundError("Invalid Directory Path")

        print("\nScanning Directory...\n")

        for root, dirs, files in os.walk(path):

            level = root.replace(path, "").count(os.sep)

            indent = " " * 4 * level

            print(f"{indent}{os.path.basename(root)}/")

            sub_indent = " " * 4 * (level + 1)

            for f in files:
                print(f"{sub_indent}{f}")

            if not files and not dirs:
                raise MissingFileOrFolderError(
                    f"Empty folder detected: {root}"
                )

    except FileNotFoundError as e:

        print("Error:", e)

    except MissingFileOrFolderError as e:

        print("Custom Error:", e)

    except Exception as e:

        print("Unexpected Error:", e)


def directory_scanning():

    print("\n===== DIRECTORY SCANNING =====")

    path = input("Enter directory path: ")

    scan_directory(path)


# =========================================================
# MODULE 8
# Performance Analysis using NumPy, Pandas, Matplotlib
# =========================================================

def performance_analysis():

    print("\n===== PERFORMANCE ANALYSIS =====")

    data = {
        "Name": ["Maddie", "Nate", "Jules", "Rue"],
        "Math": [85, 92, 76, 89],
        "Science": [88, 95, 80, 91],
        "English": [90, 89, 84, 93]
    }

    df = pd.DataFrame(data)

    print("\n--- Raw Data ---")
    print(df)

    print("\n--- Statistical Summary ---")
    print(df.describe())

    scores = df[["Math", "Science", "English"]].to_numpy()

    mean_scores = np.mean(scores, axis=0)
    median_scores = np.median(scores, axis=0)
    std_scores = np.std(scores, axis=0)

    print("\n--- NumPy Analysis ---")

    print("Mean Scores:", mean_scores)
    print("Median Scores:", median_scores)
    print("Standard Deviation:", std_scores)

    # Top performers

    top_math = df.loc[df["Math"].idxmax(), "Name"]
    top_science = df.loc[df["Science"].idxmax(), "Name"]
    top_english = df.loc[df["English"].idxmax(), "Name"]

    print("\n--- Top Performers ---")

    print("Math:", top_math)
    print("Science:", top_science)
    print("English:", top_english)

    # Graph 1

    subjects = ["Math", "Science", "English"]

    plt.bar(subjects, mean_scores)

    plt.title("Average Scores per Subject")

    plt.xlabel("Subjects")
    plt.ylabel("Average Score")

    plt.show()

    # Graph 2

    df.plot(x="Name", y=["Math", "Science", "English"], kind="bar")

    plt.title("Student Performance Comparison")

    plt.ylabel("Scores")

    plt.show()


# =========================================================
# MAIN MENU
# =========================================================

while True:

    print("\n")
    print("=================================================")
    print(" SMART CAMPUS DIGITALIZATION SYSTEM ")
    print("=================================================")

    print("1. Student Registration and Grade Evaluation")
    print("2. Course Enrollment Management")
    print("3. Student Record Management")
    print("4. Sorting and Searching Student IDs")
    print("5. Student Fee Calculation")
    print("6. File Handling for Academic Records")
    print("7. Directory Scanning")
    print("8. Student Performance Analysis")
    print("9. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        student_registration()

    elif choice == "2":
        course_enrollment()

    elif choice == "3":
        student_records()

    elif choice == "4":
        sorting_searching()

    elif choice == "5":
        fee_management()

    elif choice == "6":
        file_handling()

    elif choice == "7":
        directory_scanning()

    elif choice == "8":
        performance_analysis()

    elif choice == "9":

        print("\nThank You for using Smart Campus System")
        break

    else:

        print("\nInvalid Choice! Please try again.")
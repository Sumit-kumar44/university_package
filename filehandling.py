
import csv 
"""
with open("student.csv", "r") as file:

    csv_reader = csv.reader(file)


    for row in csv_reader:
        print(row)

"""



# writing a csv file

new_student = ["kaushal", "verma", "167656775"]

with open("student.csv", "a") as file:
    csv_writer = csv.writer(file)

    csv_writer.writerow(new_student)
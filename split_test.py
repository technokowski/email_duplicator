import csv, os
from iteration_utilities import duplicates

all_the_date = []
full_names = []
duplicate_accounts = []
wrong_emails = []

amount_of_wrongsies = 0

def email_checker(email):
    count = 0
    list_email = list(email)
    for item in list_email:
        if (item.isdigit()):
            count = count + 1
    if count == 5:
        return True
    else:
        return False

def combine_names(first, last):
    complete = first + " " + last
    full_names.append(complete)

def find_duplicates():
    test = duplicates(full_names)
    for i in test:
        duplicate_accounts.append(i)


def write_to_file(student,duplicates):
    with open('student_data.csv', mode='w') as student_data:
        student_writer = csv.writer(student_data, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for i in student:
            student_writer.writerow(i)
        for i in duplicates:
            print(i)
            student_writer.writerow([i])

with open('AllStudents2020.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    for row in csv_reader:
        first_name = row[0]
        last_name = row[1]
        email_address = row[2]
        active_suspended = row[3]
        has_logged_in = row[4]
        combine_names(first_name,last_name)
        incorrect_email = email_checker(email_address)
        if incorrect_email == True:
            print(email_address)
            amount_of_wrongsies = amount_of_wrongsies + 1
            wrong_emails.append(row)
    find_duplicates()
    write_to_file(wrong_emails, duplicate_accounts)

    print(amount_of_wrongsies)
    print(len(duplicate_accounts))


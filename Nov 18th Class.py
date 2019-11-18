import csv
import os


def display_book_list(fname):
    with open(fname, newline = "") as file_reader:
        reader = csv.reader(file_reader)
        for index, line in enumerate(reader):
            print(str(index + 1), line[0], "written by", line[1], "and was published in", line[2])


user_enter = input("File name:\t") + ".csv"

if os.path.exists(user_enter):
    print("File Found")
    user_choice = input("Would you like to view the file?(Y)")
    if user_choice.lower() == "y":
        with open(user_enter) as file_reader:
            reader = csv.reader(file_reader)
            for index, line in enumerate(reader):
                print(str(index + 1), ".", line[0], "written by", line[1], "and was published in", line[2])
    else:
        print("OK.")
else:
    print("File not found. Creating file now...")
    with open(user_enter, "a", newline = "") as csv_file_writer:
        while True:
            book_name = input("Enter book name:\t")
            book_author = input("Enter book author:\t")
            book_year = input("Enter year published:\t")
            writer = csv.writer(csv_file_writer)
            writer.writerow([book_name, book_author, book_year])
            if input("CONTINUE?(Y)") != "Y":
                break

if input("Would you like to view the file? (Y)") == "Y":
    display_book_list(user_enter)


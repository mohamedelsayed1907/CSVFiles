import os
import csv

lib_database_file_name = input("Please enter file name:\t") + ".csv"
if os.path.exists(lib_database_file_name):
    print("File Exists.")
else:
    lib_fh = open(lib_database_file_name, "w")
    lib_fh.close()
    print(lib_database_file_name, " has been created")


while True:
    book_name = input("Enter book name:\t")
    book_author = input("Enter book author:\t")
    book_year = input("Enter year published:\t")
    with open(lib_database_file_name, "a") as database_file_handler:
        csv_writer = csv.writer(database_file_handler)
        csv_writer.writerow([book_name, book_author, book_year])
    if input("CONTINUE? (Y)") != "Y":
        break

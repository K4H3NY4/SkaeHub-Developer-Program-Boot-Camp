import csv

#specify the encoding type  utf-8 or iso-8859-1 to avoid the error
#UnicodeDecodeError: 'utf-8' codec can't decode byte 0xc8

with open("file.csv", 'r', encoding="ISO-8859-1") as file:
    csv_file = csv.DictReader(file)
    for row in csv_file:
        print(dict(row))
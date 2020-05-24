import csv
import os


def parse(file_name):
    filepath = file_name + ".csv"
    arr = []
    if os.path.exists(file_name):
        with open(filepath, "r", newline="") as file:
            try:
                reader = csv.reader(file)

                for row in reader:
                    cur_arr = row[0].split(';')

                    arr.extend(cur_arr)

                row = ''
                for letter in arr:
                    row += letter
                    if letter == '\n':
                        print(row)
                        row = ''
            except OSError:
                print("Could not open/read file:", file_name)


if __name__ == "__main__":
    # you should use not capital letters and _ between words
    name_of_five = input()
    parse(name_of_five)

import csv


def parse(file_name):
    filepath = file_name + ".csv"
    arr1 = []
    arr2 = []

    with open(filepath, "r", newline="") as file:
        # читаем файл целиком
        reader = csv.reader(file)
        '''
        Циклом for проходим по строкам 
        '''
        for row in reader:
            cur_arr = row[0].split(';')
            '''
            В этом случае вы получите список значений
            '''
            arr1.extend(cur_arr)
            '''
            Тут получится список из списков. 
            Каждый добавленный блок является списком
            '''
            # arr2.extend([cur_arr])
        row = ''
        for letter in arr1:
            row += letter
            if letter == '\n':
                print(row)
                row = ''


if __name__ == "__main__":
    # you should use not capital letters and _ between words
    name_of_five = input()
    parse(name_of_five)

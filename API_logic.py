import json
import csv


def main():
    input_attribute = read_input_file()
    input_list = structure_list(input_attribute)


def read_input_file():
    # input file is file send to api
    input_file = "D:\\Documents\\Bio-informatica jaar 3\\data integratie\\input_file.txt"
    with open(input_file, 'r') as file:
        reader = csv.reader(file)
        input_attribute = []
        header = []
        row_counter = 0
        for row in reader:
            if row_counter == 0:
                header.append(row)
            else:
                input_attribute.append(row)
            row_counter += 1
    return input_attribute


def structure_list(input_attribute):
    # a structured list filled with the input data is made
    input_list = []
    for line in input_attribute:
        if len(line) == 4:
            regel = line[0] + '_' + line[1] + '_' + line[2] + '_' + line[3]
            input_list.append(regel)
            print(regel)
        else:
            # change this to api popup
            print('One or more of your entries did not contain all 4 elements, these will be ignored')
    return input_list


def return_json():
    #data = {}
    # chrom, pos, freq, ref, alt, benign, cancer = opbouw
    with open('output.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


main()

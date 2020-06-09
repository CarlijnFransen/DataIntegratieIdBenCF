import json
import csv


def main():
    header, input_attribute, row_counter = read_input_file()
    input_dict = make_dictionary(header, input_attribute, row_counter)
    calculate_frequency(input_dict)
    return_json()


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
    row_counter = row_counter - 1
    return header, input_attribute, row_counter


def make_dictionary(header, input_attribute, row_counter):
    # a dictionary filled with the input data is made
    # krijg de dict niet volledig gevuld

    # input_dict = {}
    # x = 0
    # i = 0
    # for item in header:
    #     for category in item:
    #         key = category
    #         input_dict.setdefault(key, [])
    #         while i < row_counter:
    #             input_dict[key].append(input_attribute[i][x])
    #             i += 1
    #     x += 1
    # print(input_dict)

    # weghalen als functie hierboven werkt
    input_dict = {
      "chromosome": [8, 9, 1],
      "position": [1520, 465, 13],
      "frequency": [0.0045, 0.99564, 0.00556],
      "reference_nucleotide": ["A", "C", "T"],
      "alternative_nucleotide": ["C", "G", "T"]
    }
    return input_dict


def calculate_frequency(input_dict):
    # calculate cancer frequency and generate notification for now
    cancer_freq = {}
    freq = input_dict.get('frequency')
    x = 0
    for number in freq:
        cancer_freq[x] = (1 - number)
        if 0 < cancer_freq[x] < 0.01:
            print('Dangerous!')
        x += 1
    # nog even kijken wat dit returned


def return_json():
    #data = {}
    # chrom, pos, freq, ref, alt, benign, cancer = opbouw
    with open('output.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


main()

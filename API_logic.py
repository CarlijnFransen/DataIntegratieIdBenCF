import json
import csv


def main():
    header, input_attribute, row_counter = read_input_file()
    make_dictionary(header, input_attribute, row_counter)

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
    row_counter + row_counter - 2
    return header, input_attribute, row_counter


def make_dictionary(header, input_attribute, row_counter):
    # a dictionary filled with the input data is made
    input_dict = {}
    x = 0
    for item in header:
        for category in item:
            input_dict[category] = input_attribute[0][x]
            x += 1
    print(input_dict)

# # calculate cancer frequency and generate notification for now
# cancer_freq = {}
# x = 0
# for number in freq:
#     cancer_freq[x] = (1 - number)
#     if 0 < cancer_freq[x] < 0.01:
#         print('Dangerous!')
#     x += 1
#
# # fake database for the time being
# nep_database = {
#     "chromosome": [8, 10, 4],
#     "position": [1520, 465, 752],
#     "frequency": [0.0045, 0.8872, 0.7520],
#     "reference_nucleotide": ["A", "G", "T"],
#     "alternative_nucleotide": ["C", "H", "T"]
# }
#
# #  data = {
# #      "chromosomes": chrom,
# #      "positions": pos,
# #      "frequence": freq,
# #      "reference": ref,
# #      "alternative": alt
# #
#
# #  with open('output.json', 'w', encoding='utf-8') as f:
# #      json.dump(data, f, ensure_ascii=False, indent=4)


main()

import csv
from collections import defaultdict

def parser1(file_name, dict):
    with open(file_name, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            dict[line['NAME']]['LEG_LENGTH'] = float(line['LEG_LENGTH'])


def parser2(file_name, dict):
    with open(file_name, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            dict[line['NAME']]['STRIDE_LENGTH'] = float(line['STRIDE_LENGTH'])
            dict[line['NAME']]['STANCE'] = line['STANCE']


def main():
    dinosaurs = defaultdict(dict) # dino name : dict{stance:, leg:, thing:}
    parser1('dataset1.csv', dinosaurs)
    parser2('dataset2.csv', dinosaurs)
    print(dinosaurs)




if __name__ == "__main__":
    main()
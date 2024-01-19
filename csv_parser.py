import csv
import math
from collections import defaultdict

def parser1(file_name, dict):
    with open(file_name, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        for line in csv_reader:
            dict[line['NAME']].append(line['LEG_LENGTH'])
    return dict

def parser2(file_name, dict):
    with open(file_name, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        for line in csv_reader:
            dict[line['NAME']].append(line['STRIDE_LENGTH'])
    return dict

def main():
    dinosaurs = defaultdict(list)
    dinosaurs = parser1('dataset1.csv', dinosaurs)
    dinosaurs = parser2('dataset2.csv', dinosaurs)
    
    

if __name__ == "__main__":
    main()

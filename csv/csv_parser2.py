import csv
from collections import defaultdict
from math import sqrt

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
    g = 9.8
    dinosaurs = defaultdict(dict) # dino name : dict{stance:, leg:, thing:}
    parser1('dataset1.csv', dinosaurs)
    parser2('dataset2.csv', dinosaurs)
    
    dino_speed = []
    for name,dct in dinosaurs.items():
        if 'STRIDE_LENGTH' in dct and 'STANCE' in dct and 'LEG_LENGTH' in dct and dct['STANCE'] == "bipedal":
            speed = ((dct['STRIDE_LENGTH'] / dct['LEG_LENGTH']) - 1) * sqrt(dct['LEG_LENGTH'] * g)
            dino_speed.append((name, speed))
    dino_speed.sort(key=lambda x:x[1])

    res = [name for name,speed in dino_speed]
    print(res)

if __name__ == "__main__":
    main()
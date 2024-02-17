# Given the following formula, speed = ((STRIDE_LENGTH / LEG_LENGTH) - 1) * SQRT(LEG_LENGTH * g)
# Where g = 9.8 m/s^2 (gravitational constant)


import csv
from collections import defaultdict
from math import sqrt

def parser1(file_name, dct):
    with open(file_name, 'r') as csv_file:
        csv_dct = csv.DictReader(csv_file)
        for line in csv_dct:
            dct[line['NAME']]['LEG_LENGTH'] = float(line['LEG_LENGTH'])

def parser2(file_name, dct):
    with open(file_name, 'r') as csv_file:
        csv_dct = csv.DictReader(csv_file)
        for line in csv_dct:
            dct[line['NAME']]['STRIDE_LENGTH'] = float(line['STRIDE_LENGTH'])
            dct[line['NAME']]['STANCE'] = line['STANCE']

def main():
    dinosaurs = defaultdict(dict)
    parser1('dataset1.csv', dinosaurs)
    parser2('dataset2.csv', dinosaurs)

    dino_speed = []
    for name,dct in dinosaurs.items():
        if 'STRIDE_LENGTH' in dct and 'LEG_LENGTH' in dct and 'STANCE' in dct and dct['STANCE'] == 'bipedal':
            speed = ((dct['STRIDE_LENGTH'] / dct['LEG_LENGTH'] - 1) * sqrt(dct['LEG_LENGTH'] * 9.8))
            dino_speed.append((name, speed))
    
    dino_speed.sort(key=lambda x:x[1])
    res = [name for name,speed in dino_speed]
    print(res)
    return res

if __name__ == '__main__':
    main()


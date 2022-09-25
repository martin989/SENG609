import numpy as np


class House:
    def __init__(self, sqft, num_bed, num_bath, sale_price):
        self.sqft = sqft
        self.num_bed = num_bed
        self.num_bath = num_bath
        self.sale_price = sale_price


# Create Object from File
def object_from_file(filename):
    list = []
    with open(filename) as file:
        file = open(filename, "r")
        next(file)
        cells = []
        for line in file:
            line = line.split("\n")
            cells = line[0].split(",")
            list.append(House(cells[0], cells[1], cells[2], cells[3]))
    file.close()
    return list


def getWeight(list, guessCost, addValue):
    sqf_i = 0.00000
    bed_i = 0.00000
    bath_i = 0.00000
    for h in list:
        while ((getCost(list, float(sqf_i), float(bed_i), float(bath_i)) > guessCost)):
            if ((getCost(list, float(sqf_i), float(bed_i), float(bath_i)) <= guessCost)):
                return sqf_i, bed_i, bath_i
            while ((getCost(list, float(sqf_i), float(bed_i), float(bath_i)) <= guessCost)):
                if ((getCost(list, float(sqf_i), float(bed_i), float(bath_i)) <= guessCost)):
                    return sqf_i, bed_i, bath_i
                while ((getCost(list, float(sqf_i), float(bed_i), float(bath_i)) <= guessCost)):
                    if ((getCost(list, float(sqf_i), float(bed_i), float(bath_i)) <= guessCost)):
                        return sqf_i, bed_i, bath_i
                    bath_i = bath_i + addValue
                bed_i = bed_i + addValue
            sqf_i = sqf_i + addValue


def find(list, weight_inc, cost):
    h = list[0]
    sqft_w = 0.000
    bed_w = 0.000
    bath_w = 0.000
    for sqft_w in np.arange(0.0000, float(h.sale_price), weight_inc):
        if (getCost(list, sqft_w, bed_w, bath_w) <= cost):
            return sqft_w, bed_w, bath_w, getCost(list, sqft_w, bed_w, bath_w)
        for bed_w in np.arange(0.0000, float(h.sale_price), weight_inc):
            if (getCost(list, sqft_w, bed_w, bath_w) <= cost):
                return sqft_w, bed_w, bath_w, getCost(list, sqft_w, bed_w, bath_w)
            for bath_w in np.arange(0.0000, float(h.sale_price), weight_inc):
                if (getCost(list, sqft_w, bed_w, bath_w) <= cost):
                    return sqft_w, bed_w, bath_w, getCost(list, sqft_w, bed_w, bath_w)
                print("sqft " + str(sqft_w) + " bed " + str(bed_w) + " bath " + str(bath_w) + " cost " + str(
                    getCost(list, sqft_w, bed_w,
                            bath_w)))


def getCost(list, weight_sqft, weight_bed, weight_bath):
    sum = 0.00000
    for h in list:
        sqft_guess = float(h.sqft) * float(weight_sqft)
        bed_guess = float(h.num_bed) * float(weight_bed)
        bath_guess = float(h.num_bath) * float(weight_bath)
        guess = sqft_guess + bed_guess + bath_guess
        sum = sum + (float(guess) - float(h.sale_price))
    return float(sum) ** 2 / (len(list) * 2)


def main():
    list = object_from_file(r"C:\Users\Martin\Desktop\Masters\Fall 2022 SENG-609\Week 2\house_data.csv")
    costGuess = 100
    starting_weight = 10000;
    weight_sqft, weight_bed, weight_bath, found_cost = find(list, starting_weight, costGuess)
    print("Sqft weight is: " + str(weight_sqft))
    print("Bed weight is: " + str(weight_bed))
    print("Bath weight is: " + str(weight_bath))


if __name__ == '__main__':
    main()

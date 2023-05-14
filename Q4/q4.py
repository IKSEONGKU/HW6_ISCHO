import matplotlib.pyplot as plt
import csv

def show_get_on(get_on, station):
    
def show_get_off(get_off, station):

def show_get_sum(get_sum, station):
    

def main():
    f = open("2023년 03월  교통카드 통계자료.cvs")
    data = csv.reader(f)
    next(data)
    next(data)

    station = []
    get_on = []
    get_off = []
    get_sum = []

    for row in data:
        station.append(row[3])
        get_on.append(int(row[4])+int(row[6]))
        get_off.append(int(row[5])+int(row[7]))
        get_sum.append(get_on[len(get_on)]+get_off[len(get_off)])

    tmp = 0
    for i in 
        
    plt.hist(
    



if __name__ == "__main__":
    main()

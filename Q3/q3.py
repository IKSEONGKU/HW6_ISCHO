import matplotlib.pyplot as plt
import csv


def show(year, num_male, num_female, rate_female):
    plt.title('1')
    plt.subplot(1,2,1)
    plt.title('number of male, female of Jeju')
    plt.plot(year, num_male,label = "male", marker = '.')
    plt.plot(year, num_female, label = "female", marker = '.')
    plt.xlabel('year')
    plt.ylabel('numbers')

    plt.legend()

    plt.subplot(1,2,2)
    plt.title('rate of female of Jeju')
    plt.plot(year, rate_female, label = "rate of female", marker = '.')
    plt.plot(year, [50]*len(year), label = '50 %', color = 'black')
    plt.xlabel('year')
    plt.ylabel('rate')

    plt.legend()
    plt.show()

def main():
    f = open('행정구역_시군구_별__성별_인구수_20230514154506.csv')
    data = csv.reader(f)
    next(data)
    next(data)
    year = []
    num_male = []
    num_female = []

    rate_male = []
    rate_female = []
    
    for row in data:
        year.append(row[0][2:])
        male = int(row[1])
        female = int(row[2])
        num_male.append(male)
        num_female.append(female)
        
        rate_female.append(female*100 / (male+female))
        
    show(year, num_male, num_female, rate_female)
    show(year[0:10], num_male[0:10], num_female[0:10], rate_female[0:10])
    show(year[10:20], num_male[10:20], num_female[10:20], rate_female[10:20])
    show(year[20:], num_male[20:], num_female[20:], rate_female[20:])

    

if __name__ == '__main__':
    main()

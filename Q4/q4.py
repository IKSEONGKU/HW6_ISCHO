import matplotlib.pyplot as plt
import csv

def show_get_on(get_on, station):
    plt.title('승차')
    plt.rc('font', family = 'Malgun Gothic')
    plt.rcParams['axes.unicode_minus'] = False
    plt.bar(station, get_on)
    plt.ylabel('인원수')
    plt.xlabel('역')
    plt.show()
def show_get_off(get_off, station):
    plt.title('하차')
    plt.rc('font', family = 'Malgun Gothic')
    plt.rcParams['axes.unicode_minus'] = False
    plt.bar(station, get_off)
    plt.ylabel('인원수')
    plt.xlabel('역')
    plt.show()
def show_get_sum(get_sum, station):
    plt.title('승하자 합계')
    plt.rc('font', family = 'Malgun Gothic')
    plt.rcParams['axes.unicode_minus'] = False
    plt.bar(station, get_sum)
    plt.ylabel('인원수')
    plt.xlabel('역')
    plt.show()

def main():
    f = open("2023년 03월  교통카드 통계자료.csv", encoding = 'utf-8')
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
        get_sum.append(get_on[-1]+get_off[-1])

    print(station)

    tmp = 0
    temp = ''
    station_on = station
    station_off = station
    station_sum = station
   
    
    for i in range(30):
        for j in range(len(get_on)):
            if get_on[i] < get_on[j]:
                tmp = get_on[i]
                get_on[i] = get_on[j]
                get_on[j] = tmp

               
                temp= station_on[i]
                station_on[i] = station_on[j]
                station_on[j] = temp
                
        for k in range(len(get_off)):
            if get_off[i] < get_off[k]:
                tmp = get_off[i]
                get_off[i] = get_off[k]
                get_off[k] = tmp

                temp= station_on[i]
                station_off[i] = station_off[k]
                station_off[k] = temp
                
        for a in range(len(get_sum)):
            if get_sum[i] < a:
                tmp = get_sum[i]
                get_sum[i] = get_sum[a]
                get_sum[a] = tmp

                temp= station_on[i]
                station_sum[i] = station_sum[a]
                station_sum[a] = temp
                

    
    show_get_on(get_on[:30], station_on[:30])
    show_get_off(get_off[:30], station_off[:30])
    show_get_sum(get_sum[:30], station_sum[:30])



if __name__ == "__main__":
    main()

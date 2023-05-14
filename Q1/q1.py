import matplotlib.pyplot as plt
import csv


def main():
    #전국
    f_korea = open('Korea.csv')
    data = csv.reader(f_korea)
    next(data)
    Korea =[]
    for row in data:
        Korea.append(float(row[2]))
    f_korea.close()

    #서울
    f_seoul = open('Seoul(108).csv')
    data = csv.reader(f_seoul)
    next(data)
    Seoul =[]
    for row in data:
        Seoul.append(float(row[2]))
    f_seoul.close()

    #대전
    f_daejeon = open('Daejeon(133).csv')
    data = csv.reader(f_daejeon)
    next(data)
    Daejeon =[]
    for row in data:
        Daejeon.append(float(row[2]))
    f_daejeon.close()
    
    #부산
    f_busan = open('Busan(159).csv')
    data = csv.reader(f_busan)
    next(data)
    Busan =[]
    for row in data:
        Busan.append(float(row[2]))
    f_busan.close()

    #제주
    f_jeju = open('Jeju.csv')
    data = csv.reader(f_jeju)
    next(data)
    Jeju =[]
    for row in data:
        Jeju.append(float(row[2]))
    f_jeju.close()

    print(Korea, Seoul, Daejeon, Busan, Jeju)
    month = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

    plt.subplot(2,1,1)
    plt.title('temperature')
    plt.plot(month, Korea, color = 'skyblue', label='Korea', marker = '.')
    plt.plot(month, Seoul, color = 'pink', label='Seoul(108)', marker = '.', ls = '--')
    plt.plot(month, Daejeon, color = 'green', label='Daejeon(133)', marker = '.', ls = '--')
    plt.plot(month, Busan, color = 'purple', label='Busan(159)', marker = '.', ls = '--')
    plt.plot(month, Jeju, color = 'brown', label='Jeju', marker = '.', ls = '--')
    plt.ylabel('temperature (°C)')
    plt.xlabel('month')

    plt.legend()

    Seoul_diff = []
    Daejeon_diff = []
    Busan_diff = []
    Jeju_diff = []

    for i in range(len(month)):
        Seoul_diff.append(Seoul[i] - Korea[i])
        Daejeon_diff.append(Daejeon[i]-Korea[i])
        Busan_diff.append(Busan[i]-Korea[i])
        Jeju_diff.append(Jeju[i]-Korea[i])
    
    plt.subplot(2,1,2)
    plt.title('temperature difference')
    plt.plot(month, [0]*12, color = 'black', label = '0', marker = '.', ls = '--')
    plt.plot(month, Seoul_diff, color = 'pink', label='Seoul(108)', marker = '.', ls = '--')
    plt.plot(month, Daejeon_diff, color = 'green', label='Daejeon(133)', marker = '.', ls = '--')
    plt.plot(month, Busan_diff, color = 'purple', label='Busan(159)', marker = '.', ls = '--')
    plt.plot(month, Jeju_diff, color = 'brown', label='Jeju', marker = '.', ls = '--')
    plt.ylabel('temperature diff')
    plt.xlabel('month')

    plt.legend()
    
    plt.tight_layout()
    plt.show()

    
    

if __name__ == '__main__':
    main()


    

import matplotlib.pyplot as plt
import csv

def show_frequency(list, name):
    plt.subplot(2,2,1)
    plt.hist(list[0], bins = 6, color = 'skyblue', label=name[0])
    plt.xlabel('dice number')
    plt.ylabel('frequency')
    plt.title('100 tries')

    plt.subplot(2,2,2)
    plt.hist(list[1], bins=6, color = 'red', label=name[1])
    plt.xlabel('dice number')
    plt.ylabel('frequency')
    plt.title('1000 tries')

    plt.subplot(2,2,3)
    plt.hist(list[2], bins=6, color = 'purple', label=name[2])
    plt.xlabel('dice number')
    plt.ylabel('frequency')
    plt.title('10000 tries')

    plt.subplot(2,2,4)
    plt.hist(list[3], bins=6, color = 'orange', label=name[3])
    plt.xlabel('dice number')
    plt.ylabel('frequency')
    plt.title('100000 tries')

    plt.tight_layout()
    plt.show()


def show_prob(list):
    prob = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
    cnt = 0
    
    for sub_list in list:
        for num in sub_list:
            prob[cnt][int(num)-1] += 1
        if cnt >= 3:
            break
        else:
            cnt += 1

    tmp = 100
    for i in range(4):
        for j in range(6):
            prob[i][j] /= tmp
        tmp *= 10
       
    print(prob)

    
    tries = ['100','1,000','10,000','100.000']
    plt.title('events / total tries')
    plt.plot(tries,[prob[0][0], prob[1][0], prob[2][0], prob[3][0]], label = '1')
    plt.plot(tries,[prob[0][1], prob[1][1], prob[2][1], prob[3][1]], label = '2')
    plt.plot(tries,[prob[0][2], prob[1][2], prob[2][2], prob[3][2]], label = '3')
    plt.plot(tries,[prob[0][3], prob[1][3], prob[2][3], prob[3][3]], label = '4')
    plt.plot(tries,[prob[0][4], prob[1][4], prob[2][4], prob[3][4]], label = '5')
    plt.plot(tries,[prob[0][5], prob[1][5], prob[2][5], prob[3][5]], label = '6')
    plt.xlabel('tries')
    plt.ylabel('probability of events')

    plt.legend()
    plt.show()

def main():
    f = open('q2.csv', 'r')
    data = csv.reader(f)

    name = []
    list = []
    for row in data:
        if len(row) == 1:
            name.append(row)
        else:
            list.append(row)

    f.close()

    list[3] = sum(list[3:], [])

    show_frequency(list, name)
    show_prob(list)
    

    

        
if __name__ == '__main__':
    main()

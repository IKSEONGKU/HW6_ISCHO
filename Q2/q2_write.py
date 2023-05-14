import random
import csv

def main():
    two_square_tries = []
    three_square_tries = []
    four_square_tries = []
    five_square_tries = []

    list = [two_square_tries, three_square_tries, four_square_tries, five_square_tries]

    square = 1
    for tries in list:
        square += 1
        for i in range(10**square):
            tries.append(random.randint(1,6))
        tries.sort()

    f = open('q2.csv', 'w', newline = '')
    writer = csv.writer(f)
    square = 1
    for tries in list:
        square += 1
        writer.writerow([str(10**square)+"tries"])
        while len(tries) > 10000:
            writer.writerow(tries[:10000])
            tries = tries[10000:]
        writer.writerow(tries)

    f.close()

if __name__ == '__main__':
    main()

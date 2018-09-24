from parserr import parse
from init import init
from print import printBoard
from hill_climbing import hillClimbing
from simulated_annealing import simulated_annealing
from genetic_algorithm import genetic_algorithm

def main():
    print("TUBES I IF3170 INTELIGENSI BUATAN")
    print("Masukkan nama file: ")
    namafile = input()
    states = parse(namafile)

    stop = False
    while (not stop):
        print("Tentukan Algoritma Penyelesaian:")
        print("1. Hill Climbing")
        print("2. Simulated Annealing")
        print("3. Genetic Algorithm")
        print("4. Exit")

        algo = input("Pilihan: ")

        if (algo=='1'):
            print("BOARD AWAL")
            hillClimbing(states)
            input()
        elif (algo=='2'):
            print("BOARD AWAL")
            simulated_annealing(states)
        elif (algo=='3'):
            print("BOARD AWAL")
            genetic_algorithm(states)
        elif (algo=='4'):
            print('Program selesai')
            stop = True
        else:
            print('Invalid input')

    


if __name__ == '__main__':
    main()
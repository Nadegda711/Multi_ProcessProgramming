import time
from multiprocessing import Pool
import os

def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line.strip())


if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]  # Замените на свои названия файлов


    start_time = time.time()
    for name in filenames:
        read_info(name)
    linear_time = time.time() - start_time
    print(f"{linear_time:.6f} (линейный)")


    start_time = time.time()
    with Pool() as pool:
        pool.map(read_info, filenames)
    multiprocessing_time = time.time() - start_time
    print(f"{multiprocessing_time:.6f} (многопроцессный)")

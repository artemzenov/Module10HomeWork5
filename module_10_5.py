from time import time
from multiprocessing import Pool


def read_info(name):
    all_data = list()
    with open(name, 'r', encoding='utf-8') as file:
        for line in file:
            all_data.append(line)
    print(f'файл "{name}": прочитано {len(all_data)} строк')


if __name__ == '__main__':

    filenames = [f'file {number}.txt' for number in range(1, 5)]

    # Линейный подход
    start = time()
    for i_file in filenames:
        read_info(i_file)
    end = time()
    print(f'продолжительность выполнения: '
          f'{round(end - start, 4)} секунд (линейный)')

    # Процессорный подход
    start = time()
    with Pool() as pool:
        pool.map(read_info, filenames)
    end = time()
    print(f'продолжительность выполнения: '
          f'{round(end - start, 4)} секунд (процессорный)')
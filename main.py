import time


def algorithm(list):
    sorted = False
    while not sorted:
        changed = False
        for i in range(len(list) - 1):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
                changed = True
        print(list)
        if not changed:
            sorted = True
    print(f'Sorted list: {list}')
            

def main():
    unsorted_list = []
    data = open('data.txt')
    for value in data:
        unsorted_list.append(int(value))

    start = time.perf_counter()

    algorithm(unsorted_list)

    end = time.perf_counter()
    print(f'Values in list: {len(unsorted_list)}\nTime: {end - start}')


if __name__ == '__main__':
    main()

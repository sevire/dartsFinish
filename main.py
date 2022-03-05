numbers = range(1, 20)
singles = [candidate for candidate in numbers] + [25]
doubles = [candidate * 2 for candidate in singles]
trebles = [candidate * 3 for candidate in range(1, 20)]
darts = singles + doubles + trebles

def is_double(candidate):
    return candidate in doubles

def print_finish(finish):
    for num, dart in finish:
        print(f"Dart {num}: {dart}")
        if num == len(finish):
            # This is the last dart so must be double
            print(f"Dart {num}: D{dart/2}")

def calculate_finishes(finish, num_darts):
    finishes = []
    num_darts = 3
    for dart1 in darts:
        if dart1 < finish:
            finishes.append(dart1)




def main():
    for finish in range(1, 180):
        calculate_finishes(finish)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

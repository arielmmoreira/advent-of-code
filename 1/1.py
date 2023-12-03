def main():
    file = "1/input.txt"
    input = get_input(file)

    print("Answer:", get_calibration_value(input))


def get_input(file):
    with open(file, 'r') as f:
        input = f.read().split('\n')

    return input


def get_calibration_value(input):
    sum_of_values = 0

    for word in input:
        sum_of_values += get_number_from_words(word)

    return sum_of_values  


def get_number_from_words(word):
    number = ''
    for letter in word:
        if letter.isdigit():
            number += letter

    if len(number) == 1:
        number = number * 2
    else:
        number = number[0] + number[-1]

    return int(number)

main()
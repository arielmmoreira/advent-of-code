def main():
    file = "input.txt"
    problem_input = get_input(file)

    print("Answer:", get_calibration_value(problem_input))


def get_input(file):
    with open(file, 'r') as f:
        return f.read().split('\n')


def get_calibration_value(problem_input):
    sum_of_values = 0

    for word in problem_input:
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
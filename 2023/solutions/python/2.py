def main():
    file = "../../resources/input.txt"
    problem_input = get_input(file)

    print("Answer:", get_calibration_value(problem_input))


def get_calibration_value(problem_input):
    sum_of_values = 0

    for word in problem_input:
        sum_of_values += get_digit_from_words(word)

    return sum_of_values


def get_digit_from_words(word):
    tmp_word = word
    array = [-1] * len(word)
    digits = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

    for digit in digits.keys():
        for i in range(len(word)):
            if word.startswith(digit, i):
                array[i] = digits[digit]

    for i in range(len(word)):
        if word[i].isdigit():
            array[i] = word[i]

    array = list(filter(lambda x: x != -1, array))
    digits = ''
    if len(array) == 1:
        array.append(array[0])

    digits += str(array[0]) + str(array[-1])

    print(word, array, digits)

    return int(digits)


def get_input(file):
    with open(file, 'r') as f:
        return f.read().split('\n')


main()

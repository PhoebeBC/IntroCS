def generate_triangle_numbers(number_list):
    # Generating list of triangle numbers
    list_of_triangle_numbers = []
    num = 1
    triangle_num = 1
    # Ensuring list of triangle number is no bigger than is necessary
    while triangle_num < max(number_list):
        triangle_num = int(num * (num + 1) / 2)
        list_of_triangle_numbers.append(triangle_num)
        num += 1
    return list_of_triangle_numbers


def decode(coded_file):
    with open(coded_file, 'r') as file:
        # Read each line of the file
        coded_file_list_number = []
        coded_file_list_word = []
        for line in file:
            # Convert each line to a string
            number_and_word = line.strip()
            # Convert string to a list of 2 elements, the number and associated word
            number_and_word_list = number_and_word.split()
            # add all numbers to a number list
            coded_file_list_number.append(int(number_and_word_list[0]))
            # add all words to a word list so the corresponding numbers and words will hve the same index
            coded_file_list_word.append(number_and_word_list[1])

    # Generating list of triangle numbers
    list_of_triangle_numbers = generate_triangle_numbers(coded_file_list_number)

    # Decoding message
    decoded_message = ""
    for triangle_num in list_of_triangle_numbers:
        # getting index of triangle numbers in number list
        index = coded_file_list_number.index(triangle_num)
        # getting corresponding word for number and adding to decoded message
        decoded_message += coded_file_list_word[index] + " "
        if triangle_num == max(list_of_triangle_numbers):
            # removing space from final word
            decoded_message = decoded_message.rstrip()

    return decoded_message


print(decode('coding_qual_input.txt'))

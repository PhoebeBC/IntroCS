from CaesarCipher import Caesar
from fibonacci import fibonacci, short_fib


def adding(num1, num2):
    try:
        num1 = float(num1)
        num2 = float(num2)
        result = num1 + num2
    except ValueError:
        result = "You must enter two numbers."
    return result


def check_input_integer(num):
    result = True
    while result:
        try:
            num = int(num)
            result = False
        except ValueError:
            print("You must enter a number.")
            num = input("What is your number?")
    return num


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(adding(input("Type your first number here:"), input("Type your second number here:")))
    word = input("What is your word?")
    rotations = check_input_integer(input("What is your number of rotations?"))
    file = open("plain.txt", "r")
    secret_file = open("secret.txt", "w+")
    decoded_file = open("decoded.txt", "w+")

    ciphering = Caesar(file, secret_file, decoded_file)
    o_r = rotations
    ciphering.encode_to_file(rotations)
    secret_file.close()

    if input("Would you like to undo the cipher? Y / N\n") == "Y":
        ciphering.file_handle_secret = open("secret.txt", "w+")
        ciphering.decode_to_file(rotations)
        secret_file.close()

    file.close()
    decoded_file.close()

    # length_of_fib = check_input_integer(input("How many fibonacci numbers do you want?"))
    # print(f"Sort: {short_fib(length_of_fib)}")
    # print(fibonacci(length_of_fib))



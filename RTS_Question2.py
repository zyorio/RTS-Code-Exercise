def process_input():
    '''
    Takes and validates user input for original string and number of
    characters the string will be rotated by.
    :return: string input_string: String provided by user input.
    :return: int shift: amount of characters the string will be rotated by
                    provided by the user.
    '''
    input_string = input("Please provide a string: ")
    if len(input_string) < 1:
        print("String must have one or more characters!")
        process_input()

    try:
        shift = int(input("Please provide a shift amount: "))
        if shift < 0:
            print("Shift amount must be zero or greater! ")
            process_input()

        # when shift is larger than string length, use mod to perform shift with
        if shift > len(input_string):
            shift = shift % len(input_string)

    except:
        print("Shift amount must be an integer!")
        process_input()

    return input_string, shift


def string_scramble(message, shift):
    '''
    Performs the string rotation using substrings and prints the new string
    :param string message: original message string given by user
    :param int shift: amount of characters the string will be altered by
    '''
    body = message[:len(message) - shift]
    append = message[len(message) - shift:]
    print(append + body)


def main():
    input_string, shift = process_input()
    string_scramble(input_string, shift)


if __name__ == "__main__":
    main()

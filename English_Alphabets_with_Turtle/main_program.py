import project_module.english_alphabets as ea


def input_valid():
    message = ''
    while not message.isalpha():
        message = input("Enter English letters to dislpay: ")
    return message


if __name__ == "__main__":
    message = input_valid()
    ea.draw(message)


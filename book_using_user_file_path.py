def main():
    file_path = input("enter the file path to desired book: ")
    text = get_file_text(file_path)
    print(text)


def get_file_text(path):
    with open(path) as file:
        return file.read()


main()
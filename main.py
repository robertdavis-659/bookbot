def main():
    file_path = "books/frankenstein.txt"
    text = get_file_text(file_path)
    word_count = get_word_count(text)
    print(text)
    print(f"This file contains {word_count} word(s)")


def get_file_text(path):
    with open(path) as file:
        return file.read()


def get_word_count(text):
    words = text.split()
    return len(words)


main()
def main():
    file_path = "books/frankenstein.txt"
    text = get_file_text(file_path)
    word_count = get_word_count(text)
    character_counts = get_character_counts(text)
    letter_counts = get_sorted_letter_counts(character_counts)
#    print(text)
    print(f"--- Begin report of {file_path} ---")
    print(f"This file contains {word_count} word(s)")
#    print(character_counts)
#    print(letter_counts)
# This for loop iterates over the keys in the letter_counts dictionary to print an f-string for each key/value pair in the dictionary
    for keys in letter_counts.keys():
        print(f"The letter '{keys}' appears {letter_counts[keys]} times")
    print("--- End report ---")

# This function takes a provided file path and returns a string of the file's contents.
# main() sets the variable "text" to the string returned by this function.
def get_file_text(path):
    with open(path) as file:
        return file.read()

# This function takes a provided string and splits the string into a list of individual words called words.
# It then returns the length of the words list (count of items in the list).
# main() sets the variable "word_count" to the number returned by this function.
def get_word_count(text):
    words = text.split()
    return len(words)

# This function takes a provided string and converts it into a list of characters. Those characters are corrected to be in all lower case.
# It then creates a dicationary (character_counts) by iterating over the list to add each unique character to the dictionary as a key with a value of 0.
# The function loops over each character in the characters list and increments the value for that character in the dictionary.
# This function returns the dictionary character_counts which has a key for each unique character in the provided text and a value counting each time that character appeared in the text.
# main() sets the variable character_counts to the dictionary returned by this function
def get_character_counts(text):
    characters = list(text.lower())
    character_counts = {char:0 for char in characters}
    for char in characters:
        character_counts[char] += 1
    return character_counts

# This function takes a provided dictionary and sorts it by the number of times each letter appears in the text.
# First it creates an empty dictionary to store the output.
# Then it iterates over the provided dictionary and checks to see if the key is a letter. Only letters are added to the empty dictionary
# After creating a dictionary containing only the letters from the provided dictionary, it sorts the new dictionary by the value in descending order.
# The function then returns the sorted dictionary.
# main() sets the variable letter_counts to the dictionary returned by this function
def get_sorted_letter_counts(character_counts):
    letter_counts = {}
    for key, value in character_counts.items():
        if key.isalpha() == True:
            letter_counts[key] = value
    letter_counts = {key: value for key, value in sorted(letter_counts.items(), key=lambda kv: (kv[1], kv [0]), reverse = True)}
    return letter_counts

main()
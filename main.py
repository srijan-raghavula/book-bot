def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
    words = file_contents.split()
    words_count = countWords(words)
    frequency = charCount(file_contents)
    print("Welcome to BookBot")
    print(f"There are a total of {words_count} words in the book.")
    print()
    print("The character frequency in the book:")
    for char in frequency:
        if char.isalpha():
            print(f"{char} was found {frequency[char]} times.")
    print("END")


def countWords(words):
    count = len(words)
    return count


def charCount(file_contents):
    charfreq = {}
    for char in file_contents:
        char = char.lower()
        if char in charfreq:
            charfreq[char] += 1
        else:
            charfreq[char] = 1
    return charfreq


main()

with open("books/frankenstein.txt") as f:
    file_contents = f.read()
alphabet = "abcdefghijklmnopqrstuvwxyz"
def main():
    print(file_contents)
    # ...
    words = file_contents.split()
    print(len(words))
    lowfile = file_contents.lower()
    letters = {}
    for char in lowfile:
        if char in letters:
            letters[char] += 1
        else:
            letters[char] = 1

    for c in alphabet:
        print(f"The '{c}' character was found {letters[c]} times")

main()

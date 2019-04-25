from sys import argv, exit
import fileinput


def main():
    #if len(argv) != 2:
        #print("Usage: python bleep.py dictionary.txt")
        #exit(1)
    #else:
        #dictionary = argv[1]
    dictionary = 'banned.txt'
    text = input("Enter text to bleep: ").split(" ")
    for i, word in enumerate(text):
        if word in open(dictionary).read():
            text[i] = "*"*len(word)
    print(*text)


if __name__ == "__main__":
    main()

from helpers import alphabet_position, rotate_character

def encrypt(text, rot):
    newStr = ""
    for i in text:
        newChar = rotate_character(i, rot)
        newStr = newStr + newChar
    return newStr

def main():
    text = input("Type a message: ")
    rot = int(input("Rotate by: "))
    return encrypt(text, rot)

if __name__ == "__main__":
    main()

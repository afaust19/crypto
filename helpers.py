def alphabet_position(letter):
    letter = letter.lower()
    return ord(letter) - 97

def rotate_character(char, rot):
    lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    newStr = ""
    if char in lower_alphabet:
        idx = alphabet_position(char)
        newStr += lower_alphabet[(idx + rot) % 26]
    if char in upper_alphabet:
        idx = alphabet_position(char)
        newStr += upper_alphabet[(idx+rot) % 26]
    if char not in lower_alphabet and char not in upper_alphabet:
        return char
    return newStr

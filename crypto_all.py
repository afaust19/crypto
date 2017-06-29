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

def encrypt(text, rot):
    newStr = ""
    for i in text:
        newChar = rotate_character(i, rot)
        newStr += newChar
    return newStr

#def main():
#    text = input("Type a message: ")
#    rot = int(input("Rotate by: "))
#    return encrypt(text, rot)

#if __name__ == "__main__":
#    main()

def encrypt(text, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    idx = 0             #accumulator function for indices of keyword
    newStr = ""         #accumulator function for new string
    for i in text:      #iterate through each character in original message to determine if it is a non-alphabetical character
        if i in alphabet:
            newStr += (key[idx % len(key)]) #if in alphabet, replace (add to new string) each character in text with the next rotating character in key
            idx += 1                           #move on to next index in key
        if i not in alphabet:
            newStr += i                     #leave non-alphabetical character unchanged

    idx_list = []                                   #make new index list that contains all alphabet positions for new string (text replaced by key)
    for j in newStr:
        idx_pos = alphabet_position(j)              #call on alphabet_position function to find indices
        idx_list.append(idx_pos)

    finalStr = ""
    idx = 0
    for k in text:
        finalStr += rotate_character(k, idx_list[idx])    #call on rotate_character to make final encrypted string; use original text
        idx += 1                                               # chracters (k) and rotation number (idx_list[idx])
    return finalStr

#def main():
text = input("Type a message: ")
key = (input("Encryption key: "))
print(encrypt(text, key))

#if __name__ == "__main__":
#    main()

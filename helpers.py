def alphabet_position(letter):
     if (ord(letter) >= 97) and (ord(letter) <= 122):
        return ord(letter)-97
     elif (ord(letter) >= 65) and (ord(letter) <= 90):
        return ord(letter)-65
     else:
        pass
def rotate_character(letter, rot):
    shift = 97 if letter.islower() else 65
    return chr((ord(letter) + rot - shift) % 26 + shift)

def alphabet_position(letter):
     if (ord(letter) >= 97) and (ord(letter) <= 122):
        return ord(letter)-97
     elif (ord(letter) >= 65) and (ord(letter) <= 90):
        return ord(letter)-65
     else:
        pass
def rotate_character(char,rot):
    if (ord(char) >= 97) and (ord(char) <= 122):
        return chr(97+(alphabet_position(char)+rot)%26)
    elif (ord(char) >= 65) and (ord(char) <=90):
        return chr(65+(alphabet_position(char)+rot)%26)
    else:
        return char
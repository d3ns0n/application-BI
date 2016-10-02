from string import ascii_lowercase as lc, ascii_uppercase as uc

def rot(rotation_step, letter):
    origin_alphabet = lc + uc 
    rotated_alphabet = lc[rotation_step:] + lc[:rotation_step] + uc[rotation_step:] + uc[:rotation_step] # create rotated alphabet
    index = origin_alphabet.index(letter) # determine index of letter in alphabet
    return rotated_alphabet[index]

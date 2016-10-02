from string import ascii_lowercase as lc, ascii_uppercase as uc

rotation_step_enc = -3 # rotation step for encrypting messages

def rot(rotation_step, letter):
    origin_alphabet = lc + uc 
    rotated_alphabet = lc[rotation_step:] + lc[:rotation_step] + uc[rotation_step:] + uc[:rotation_step] # create rotated alphabet
    index = origin_alphabet.index(letter) # determine index of letter in alphabet
    return rotated_alphabet[index] # return letter at index in rotated alphabet
    
def encrypt(message):
    encrypted_message = ''
    for letter in message:
        encrypted_message += rot(rotation_step_enc, letter)
    return encrypted_message
    
def decrypt(message):
    decrypted_message = ''
    for letter in message:
        decrypted_message += rot(-rotation_step_enc, letter)
    return decrypted_message
    
    
    

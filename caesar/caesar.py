#!/usr/bin/env python

from string import ascii_lowercase as lc, ascii_uppercase as uc
import sys

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
    
def print_usage():
    print('Usage: caesar <command> <message>\n\n')
    print('Example: caesar encrypt "HELLO"\n')
    
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print_usage()
        sys.exit()
        
    mode = sys.argv[1]
    message = sys.argv[2]
    
    if mode == 'encrypt':
        print(encrypt(message))
        
    if mode == 'decrypt':
        print(decrypt(message))

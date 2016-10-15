#!/usr/bin/env python
# -*- coding: utf-8 -*-
from string import ascii_lowercase as lc, ascii_uppercase as uc
import sys

rotation_step_enc = -3  # rotation step for encrypting messages


def rot(rotation_step, letter):
    origin_alphabet = lc + uc
    if letter not in origin_alphabet:
        return letter
    rotated_alphabet = lc[rotation_step:] + lc[:rotation_step] + uc[rotation_step:] + uc[
                                                                                      :rotation_step]  # create rotated alphabet
    index = origin_alphabet.index(letter)  # determine index of letter in alphabet
    return rotated_alphabet[index]  # return letter at index in rotated alphabet


def encrypt(message):
    encrypted_message = ''
    for letter in message:
        encrypted_message += rot(rotation_step_enc, letter)  # rotate to encrypt message
    return encrypted_message


def decrypt(message):
    decrypted_message = ''
    for letter in message:
        decrypted_message += rot(-rotation_step_enc, letter)  # rotate in opposite direction for decryption
    return decrypted_message


def print_usage():
    print('Usage: caesar.py <command> <message> \n')
    print('Commands: decrypt, encrypt')
    print('Message: string to en- / decrypt \n')
    print('Example: caesar.py encrypt "HELLO"')


if __name__ == '__main__':
    if len(sys.argv) != 3:  # if less than 2 arguments given on command line
        print_usage()

    else:
        mode = sys.argv[1]
        message = sys.argv[2]

        if mode == 'encrypt':
            print(encrypt(message))

        elif mode == 'decrypt':
            print(decrypt(message))

        else:  # if given mode is neither encrypt nor decrypt
            print_usage()

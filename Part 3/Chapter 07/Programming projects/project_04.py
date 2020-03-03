#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@author: Pieter Huycke
email:   pieter.huycke@ugent.be
GitHub:  phuycke
"""


#%%

import string

#%%


# clean an imported text and return as a single string
def clean_text(imported_text = str):
    
    
    """
    Stripts inputted text from whitespaces and punctuations
    Lowercases the entire text
    """
    
    clean = imported_text.replace(" ", "")
    for sign in string.punctuation:
       clean = clean.replace(sign, "")
    
    return clean.lower()
 
    
# encrypt a message using a Caesars cipher  
def caesars_encrypt(to_encrypt = str, 
                    step       = int):
    
    """
    Input a string, and returns an encrypted text using Caesars cipher method
    The steps can be defined in the function
    """
    
    word_list       = list(to_encrypt.split(" "))
    encrypted_words = []
    
    for word in word_list:
        encrypted = ""
        for letter in word:
            if letter not in string.ascii_lowercase:
                continue
            if (ord(letter) + step) > ord("z"):
                encrypted += chr(ord(letter) + step - len(string.ascii_lowercase)).upper()
            else:
                encrypted += chr(ord(letter) + step).upper()
        encrypted_words.append(encrypted)
    
    return " ".join(encrypted_words)


# decrypt a message using a Caesars cipher  
def caesars_decrypt(to_decrypt = str, 
                    step       = int):
    
    """
    Decrypts a message that was originally encrypted using Caesars cipher
    The steps can again be inputted in the function
    """
    
    word_list       = list(to_decrypt.split(" "))
    decrypted_words = []
    
    for word in word_list:
        decrypted = ""
        for letter in word:
            if letter not in string.ascii_uppercase:
                continue
            letter = letter.lower()
            if (ord(letter) - step) < ord("a"):
                decrypted += chr(ord(letter) - step + len(string.ascii_lowercase))
            else:
                decrypted += chr(ord(letter) - step)
        decrypted_words.append(decrypted)
    
    return " ".join(decrypted_words)
        

def break_caesar(message       = str, 
                 most_frequent = "e"):
    
    """
    Attempts to decode an encode message based on frequency analysis
    This function relies on the hypothesis that the letter 'e' is the most
    commonly used letter in strings
    """
    
    highest_proportion = -1
    frequent_letter    = ""
    
    # get the most frequent letter
    for letter in set(message):
        if message.count(letter) > highest_proportion:
            highest_proportion = message.count(letter)
            frequent_letter    = letter
    
    # assume that this letter represents an "e"
    step = ord(frequent_letter.lower()) - ord("e")
    
    return caesars_decrypt(to_decrypt = message, 
                           step       = step)
        

#%%
   
# the string we start from
text = "lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua semper viverra nam libero justo laoreet sit amet cursus nibh ipsum consequat nisl vel pretium lectus condimentum id venenatis a condimentum vitae sapien elit eget gravida cum sociis natoque penatibus et in hendrerit gravida rutrum quisque pulvinar etiam non quam lacus aliquam faucibus purus in massa tempor nec feugiat nisl pretium blandit volutpat maecenas volutpat blandit aliquam etiam erat velit scelerisque in dictum non consectetur a sagittis orci a scelerisque purus semper at urna condimentum mattis pellentesque id nibh vitae purus faucibus ornare suspendisse libero justo laoreet sit amet cursus sit"

print("\n- - - -\nOriginal message\n- - - -\n")
print(text)

# an example of the encryption process
encrypted = caesars_encrypt(to_encrypt = text,
                            step       = 3)
print("\n- - - -\nEncrypted message using Caesar's cipher\n- - - -\n")
print(encrypted)

# an example of the decryption process
decrypted = caesars_decrypt(to_decrypt = encrypted, 
                            step       = 3)
print("\n- - - -\nDecrypted message using Caesar's cipher\n- - - -\n")
print(decrypted)

# show the code breaker
deciphered = break_caesar(message = encrypted.replace(" ", ""))
print("\n- - - -\nDecrypted message using frequency analysis\n- - - -\n")
print(deciphered)
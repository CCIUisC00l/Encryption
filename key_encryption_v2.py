encrypt = [None, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabet = "zabcdefghijklmnopqrstuvwxyz"
reverse_encrypt = {}

for index, value in zip(range(27), encrypt):
    reverse_encrypt.update({value: index})

def word_to_key(word: str) -> list:
    word_numbers = []
    for i in word:
        word_numbers.append(alphabet.find(i))
    return word_numbers


def enc(mes: str, key: list) -> str:

    key = word_to_key(key) if type(key) is str else key # for direct usability with the polyalphabetic decryption
    mes = mes.lower() # conditioning the message to fit the dictionary that we have
    key_len = len(key) # getting the length of the key and the message
    mes_len = len(mes)
    # key_len_mul_whole = round(mes_len/key_len) # Store the number of times that the key needs to be repeated
    key_len_fract = mes_len%key_len # Stores the fraction of the whole that needs to be added inorder to make the key the same length as the message
    key_len_mul_whole = round((mes_len - key_len_fract)/key_len)

    new_key = []
    for i in range(key_len_mul_whole): # making a repeating key based on the one provided 
        new_key += key
    new_key += key[0: key_len_fract]

    encrypted_message = ''
        
    for c, i in zip(mes, new_key): # associating a number from the key with a letter from the message
    
        if c in alphabet:
            position = alphabet.find(c)
            new_position = (position + i) % 26
            new_character = alphabet[new_position]
            encrypted_message += new_character
        else:
            encrypted_message += c

    return encrypted_message


def dec(mes: str, key: list) -> str:
    # key = word_to_key(key) if type(key) is str else key # for direct usability with the polyalphabetic decryption
    mes = mes.lower() # conditioning the message to fit the dictionary that we have
    key_len = len(key) # getting the length of the key and the message
    mes_len = len(mes)
    # key_len_mul_whole = round(mes_len/key_len) # Store the number of times that the key needs to be repeated
    key_len_fract = mes_len % key_len # Stores the fraction of the whole that needs to be added inorder to make the key the same length as the message
    key_len_mul_whole = round((mes_len - key_len_fract)/key_len)

    new_key = []
    for i in range(key_len_mul_whole): # making a repeating key based on the one provided 
        new_key += key
    new_key += key[0: key_len_fract]

    encrypted_message = ''
        
    for c, i in zip(mes, new_key): # associating a number from the key with a letter from the message
    
        if c in alphabet:
            position = alphabet.find(c)
            new_position = (position - i) % 26
            new_character = alphabet[new_position]
            encrypted_message += new_character
        else:
            encrypted_message += c

    return encrypted_message

if __name__ == "__main__":

    print(word_to_key("command"))

    message = "do not go to the bridge"
    
    key1 = [3, 4, 12, 4, 25, 3, 1, 23, 14, 16, 5, 9, 11]
    key2 = [4, 5, 13, 16, 9, 25, 26, 12, 15, 7, 5, 1, 2]

    enc_message1 = enc(message, 'command')
    enc_message2 = enc(enc_message1, key2)

    dec_message2 = dec(enc_message2, key1)

    enc_message3 = enc(message, key2)

    dec_message1 = dec(dec_message2, key2)

    print(message) # ORIGINAL
    print(enc_message1) # ENCRYPT KEY1
    print(enc_message2) # ENCRYPT BOTH KEYS
    print(enc_message3) # ENCRYPT KEY2
    print(dec_message2) # DECRYPT BOTH BY KEY 1
    print(dec_message1) # DECRYPT dec_message2 BY KEY 2
    
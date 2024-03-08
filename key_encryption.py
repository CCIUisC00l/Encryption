
encrypt = [None, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
reverse_encrypt = {}
alphabet = "zabcdefghijklmnopqrstuvwxyz"
# Both lists that map numbers to letter are intended to be used with values in the keys from 1 - 26. not 0 - 25
for index, value in zip(range(27), encrypt): # Generating the reverse of the list above
    reverse_encrypt.update({value: index})

def enc(mes, key):
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
            new_position = (position - i) % 26
            new_character = alphabet[new_position]
            encrypted_message += new_character
        else:
            encrypted_message += c
                
    # icorrect = 0 # to correct for spaces throwing off the encrtiption process
    # for letter, i in zip(mes, range(mes_len)):
    #     if letter == " ": # checking for spacees and correcting the icorrect variable
    #         encrypted_message += " "
    #         icorrect += 1
    #     else:
    #         num = reverse_encrypt[letter]
    #         num += new_key[i - icorrect]
    #         if num > 26:
    #             num = num - 26
    #         elif num < 0:
    #             num = 26 - num
    #         encrypted_message += encrypt[num]

    return encrypted_message

# def rev_enc(mes, key):



if __name__ == "__main__":

    # message = input("Message >> ").lower()

    # key1 = [3, 4, 12, 4, 25, 3, 1, 23, 14, 16, 5, 9, 11]
    # key2 = [4, 5, 13, 16, 9, 25, 26, 12, 15, 7, 5, 1, 2]

    # key3 = [21]

    # enc_message1 = enc(message, key1)
    # enc_message2 = enc(enc_message1, key2)

    # dec_message2 = rev_enc(enc_message2, key2)
    # dec_message1 = rev_enc(dec_message2, key1)

    # print(message + "\n")
    # print(enc_message1 + "\n")
    # print(enc_message2 + "\n")
    # print(dec_message2 + "\n")
    # print(dec_message1 + "\n")

    # mess = input()
    thisis = "gluntlishjrvbadvyyplkaohavbyjpwolypzavvdlhruuleatl zz hnlzdpajoavcpnlulyljpwolyrlfdvykpzaolopkkluzftivsvmklhaoputfmhcuypalovsilpuluk"
    that = "vwduwljiudeehghyhubwklqjlfrxogilqgsohdvhuhwxuqdqbeoxhsalqwviruydxowdifkedqnbrxghflghrqldpvhwwlqjxsvdihkrxvhfr"
    # print(mess)
    for i in range(26):
        print(enc(thisis, [i]))
        print(enc(that, [i]), "\n\n\n")

from matplotlib import pyplot as plt
from string import ascii_lowercase
from key_encryption import enc

letterFrequency = {'e' : 12.0,
't' : 9.10,
'a' : 8.12,
'o' : 7.68,
'i' : 7.31,
'n' : 6.95,
's' : 6.28,
'r' : 6.02,
'h' : 5.92,
'd' : 4.32,
'l' : 3.98,
'u' : 2.88,
'c' : 2.71,
'm' : 2.61,
'f' : 2.30,
'y' : 2.11,
'w' : 2.09,
'g' : 2.03,
'p' : 1.82,
'b' : 1.49,
'v' : 1.11,
'k' : 0.69,
'x' : 0.17,
'q' : 0.11,
'j' : 0.10,
'z' : 0.07 }


def store_freq(message: str, usable_chars=ascii_lowercase) -> dict:
    reverse_encrypt = {} # The dictionary that will store all of the bins for histogram plotting and other stuff
    for letter in usable_chars: # iterating over all of the characters in the message (defaults to the letters in the alphabet)
        reverse_encrypt.update({letter: round(message.lower().count(letter)/len(message) * 100, 5)}) # calculating frequency in terms of a percentage for each letter
    # print(reverse_encrypt)
    return reverse_encrypt

if __name__ == "__main__":

    thisis = "gluhtlishjrvbadvyyplkaohavbyjpwolypzavvdlhruuleatlzzhnlzdpajoavcpnlulyljpwolyrlfdvykpzaolopkkluzftivsvmklhaoputfmhcuypalovsilpuluk"
    thisis = enc(thisis, [7])
    freq_bins = store_freq(thisis)

    plt.bar(freq_bins.keys(), freq_bins.values(), color='g')
    plt.bar(letterFrequency.keys(), letterFrequency.values(), color='r')
    plt.show()

        
from numpy import loadtxt
from key_encryption_v2 import enc

all_words = loadtxt("google-10000-english.txt", dtype=str) # making the list of top 10000 english words

def auto_cesear(message):

    for shift in range(26): # iterating through the list as many times as there numbers of the alphabet

        word_count = 0 # keeping track of how many words there are in a specfic decryption
        words_found = []
        should_i_break = False # keeping track of weather or not to continue trying things
        decrypting = enc(message, [shift]) # encrypting the message by a specified ceaseraen shift

        for i in all_words: # checking to see if any words are in the message

            if i in decrypting and len(i) > 3:

                word_count += 1 # adding another to the word count
                words_found.append(i)
                if word_count > 3: # checking to see if this is a real message

                    print(f">> WORD FOUND <<\nhere is the message:\n{decrypting}\nThe shift is {shift}\nThe word found is {i}\nWords found: {words_found}")

                    if "n" in input("Would you like to continue? [y/n] >> ").lower():
                        should_i_break = True
                        break

        if should_i_break:
            return decrypting, shift # returns the message and the shift    

if __name__ == "__main__":

    message2 = "vwduwljudeehghyhubwklqjlfrxogilqgsohdvhuhwxuqdqbeoxhsulqwviruydxowd qgdodupghvljqedvhgrqzklfkedqnbrxghflghrqldpvhwwlqjxsvdihkrxvhfr"
    message1 = "gluhtlishjrvbadvyyplkaohavbyjpwolypzavvdlhrvuuleatlzzhnlzdpajoavcpnlulyljpwolyrlfdvykpzaolopkkluzftivsvmklhaoputfmhcvypalovsilpuluk"
    answer1 = auto_cesear(message1)
    answer2 = auto_cesear(message2)
    # print(answer1)
    print(answer2[0] + answer1[0])

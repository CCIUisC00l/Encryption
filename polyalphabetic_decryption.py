from key_encryption_v2 import dec, enc, word_to_key, reverse_encrypt
from numpy import loadtxt
import time

common_words = loadtxt("google-10000-english/20k.txt", dtype=str)  # making the list of top 10000 english words
all_words = loadtxt("english-words/words.txt", dtype=str)

def word_to_key(word): # automating the turning of a word into a key in the format of a list
    key = [reverse_encrypt[i] for i in word]
    return key

def poly(message: str, key_word="snake", auto_pick=False, long_check=False, verbose=True):

    probability_of_right_word = []
    starttime = time.time()
    probability_threshold = len(message.split(" ")) # Storing the number of words that is contained in the message assuming spaces.

    if auto_pick: # decide weather to auto_pick a keyword or not
        possible_shifts = []
        if long_check:
            for shift_word in all_words: # iterating through the list as many times as there numbers of the alphabet

                word_count = 0 # keeping track of how many words there are in a specfic decryption
                words_found = []
                should_i_break = False # keeping track of weather or not to continue trying things
                decrypting = enc(message, word_to_key(shift_word)) # encrypting the message by a specified shift word

                for i in all_words: # checking to see if any words are in the message

                    if i in decrypting and len(i) > 3:

                        word_count += 1 # adding another to the word count
                        words_found.append(i)
                        if word_count > 3: # checking to see if this is a real message

                            print(f">> WORD FOUND <<\nhere is the message:\n{decrypting}\nThe shift word is {shift_word}\nWords found: {words_found}")

                            if "n" in input("Would you like to continue? [y/n] >> ").lower():
                                should_i_break = True
                                break
                
                if should_i_break:
                    print(f"Time to Break: {time.time() - starttime}")
                    return decrypting, shift_word if verbose else possible_shifts# returns the message and the shift   
            
                if shift_word == all_words[-1]:
                    print(f"No Message Found. Time Wasted: {time.time() - starttime}")  
                    return possible_shifts
        else:
            for shift_word in common_words: # iterating through the list as many times as there are words in the english language

                word_count = 0 # keeping track of how many words there are in a specfic decryption
                words_found = []
                should_i_break = False # keeping track of weather or not to continue trying things
                decrypting = dec(message, word_to_key(shift_word)) # encrypting the message by a specified ceaseraen shift

                for i in common_words: # checking to see if any words are in the message

                    if i in decrypting and len(i) > 3:

                        word_count += 1 # adding another to the word count
                        words_found.append(i) # This is not a necessary addition to the code...

                        if word_count == 4: # checking to see if this could be a real message
                            if verbose:
                                print(f">> WORD FOUND <<\nhere is the message:\n{decrypting}\nThe shift word is {shift_word}\nWords found: {words_found}")

                                if "n" in input("Would you like to continue? [y/n] >> ").lower():
                                    should_i_break = True
                                    break
                            else:
                                possible_shifts.append(shift_word)

                                # break # stops after the determined amount of words is defined so as to not take much time?

                probability_of_right_word.append(word_count) # storing the amount of words found in each message. This could be zipped with possible shifts to associate word and probability

                if word_count >= probability_threshold - 5 and not(verbose):
                    print(f"Time to Break: {time.time() - starttime}")
                    return zip(possible_shifts, probability_of_right_word)    
                
                if should_i_break:
                    print(f"Time to Break: {time.time() - starttime}")
                    return decrypting, shift_word if verbose else possible_shifts# returns the message and the shift  
            
                if shift_word == common_words[-1]:
                    print(f"No Message Found. Time Wasted: {time.time() - starttime}") if verbose else print(None)
                    return zip(possible_shifts, probability_of_right_word)    

                print(shift_word)
    else:
        decrypted_message = dec(mes=message, key=word_to_key(key_word))
        return decrypted_message


if __name__ == "__main__":
    plain_txt = "This is a test to see if my polyalphabetic decryption script actually works. I would be suprised if it does and then I will be happy. It will be a nightmare if it does not work"
    encrypted_message = enc(plain_txt, "command")
    # print(poly(encrypted_message, 'command'))
    print(poly(encrypted_message, auto_pick=True, verbose=False))
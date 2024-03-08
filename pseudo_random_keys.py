class keyGen():

    def __init__(self, seed, length):
        self.seed = seed
        self.seed_len = len(str(self.seed))
        self.message_len = length
        self.key_as_list = []
        self.key_as_list_len = len(self.key_as_list)



    def key_condition(self):
        icorrect = 0
        self.reverse_key()

        key_int_list = []
        for i in range(len(self.key)):
            key_int_list.append(self.key[i])

        try:
            for i in range(len(self.key)):
                digits = True if int(self.reversed_key[i]) > 4 else False
                if digits:
                    appending = self.key[i+icorrect: i+icorrect+2]
                else:
                    appending = self.key[i+icorrect]

                icorrect += 1 if digits == True else 0
                self.key_as_list.append(int(appending) % 26)
        except IndexError:
            pass
        
        self.key_as_list_len = len(self.key_as_list)

    def reverse_key(self):
        self.reversed_key = self.key[::-1]


    def middle_square(self):

        self.key = ''

        fract_len = self.message_len % self.seed_len
        iterations = round((self.message_len - fract_len) / self.seed_len) + 1

        new_seed = self.seed
        for i in range(iterations):
        
            square = str(new_seed * new_seed)
            square_len = len(square) # choosing the indexed range to concatenate to the key variable that will be returned
            square_len_difference = round((square_len - self.seed_len) / 2) # getting the number of the index to satrt grabbing from the squared number in order to get the middle of the square
            middle_square = square[square_len_difference: self.seed_len+square_len_difference] # getting the middle of the square
            self.key += middle_square
            new_seed = int(middle_square)

        self.key_len = len(self.key)

        return int(self.key)


if __name__ == "__main__":
        
    psr = keyGen(32783456782105249853462356346835623405972394856278346556, 300)
    psr.middle_square()
    print(psr.key)

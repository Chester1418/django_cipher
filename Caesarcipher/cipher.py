class CaesarCipher:
    Freqlet = {'a': 8.17, 'b': 1.5, 'c': 2.78, 'd': 4.25, 'e': 12.7, 'f': 2.23, 'g': 2.02, 'h': 6.09, 'i': 6.97,
               'j': 0.15, 'k': 0.77, 'l': 4.03, 'm': 2.41, 'n': 6.75, 'o': 7.51, 'p': 1.93, 'q': 0.1, 'r': 5.99,
               's': 6.33, 't': 9.06, 'u': 2.76, 'v': 0.98, 'w': 2.36, 'x': 0.15, 'y': 1.97, 'z': 0.07}
    letters = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    len_letters = len(letters)
    letter = ''.join(letters)

    def __init__(self, text):
        self.__text = text

    def caesar_main(self, rotation=0, encrypt=True):
        enc_text = ''
        letters_upper = [x.upper() for x in self.letters]
        symbol_present = None
        rotation = rotation if encrypt is True else rotation * -1
        for symbol in self.__text:
            if symbol in self.letters:
                symbol_present = self.letters[:]
            elif symbol in letters_upper:
                symbol_present = letters_upper
            if symbol_present:
                position = (symbol_present.index(symbol) + rotation + self.len_letters) % self.len_letters
                enc_text += symbol_present[position]
                symbol_present = None
            else:
                enc_text += symbol
        return enc_text

    def count(self, text=''):
        if not text:
            text = self.__text.lower()
        else:
            text = text.lower()
        text_len = len(text)
        count_symbols = {i: text.count(i) for i in self.letters if i in text}
        frequency = {i: round((count_symbols[i] / text_len) * 100, 3) for i in count_symbols}

        return frequency

    def brute_force(self):
        bruted= {}
        for key in range(len(self.letter)):
            translated = ''
            for symbol in self.__text:
                if symbol in self.letter:
                    num = self.letter.find(symbol)
                    num = num - key
                    if num < 0:
                        num = num + len(self.letter)
                    translated = translated + self.letter[num]
                    bruted[key] = translated
                else:
                    translated = translated + symbol
        return bruted

    def count_frequency(self, decrypted_text):
        frequency = self.count(decrypted_text)
        text_frequency = [abs((frequency[i] - self.Freqlet[i])) for i in frequency]
        return sum(text_frequency)

    def try_detect_rotation(self):
        all_frequencies = [self.count_frequency(self.caesar_main(rot, False)) for rot in range(26)]
        rotation = all_frequencies.index(min(all_frequencies))
        return rotation

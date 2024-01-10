MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}


def text_to_morse(text):
    global not_translated
    morse_code = ""
    not_in_dict = ""
    for letter in text:
        if letter in MORSE_CODE_DICT:
            morse_code += MORSE_CODE_DICT[letter]
        else:
            not_in_dict += letter
    if not not_in_dict:
        not_translated = False
        return print(morse_code)
    else:
        return print(f"The following can't be turned into morse code: {not_in_dict}")


not_translated = True
while not_translated:
    message = input("Please type the message you want to turn into morse code: ")
    text_to_morse(text=message.upper())

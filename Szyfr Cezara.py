# https://pl.spoj.com/problems/JSZYCER/
import sys
def Szyfrowanie(character_nubmer):
    if character_nubmer == 32:
        new_character_number = 32
    elif character_nubmer == 10:
        new_character_number = 10
    else:
        new_character_number = character_nubmer + 3
        if new_character_number > 90:
            new_character_number = new_character_number - 26
    return new_character_number

def Cezar(text, code=3):
    text_list = list(map(ord, text))
    text_list = list(map(Szyfrowanie, text_list))
    return "".join(list(map(chr, text_list)))
text = sys.stdin.read()
print(Cezar(text))
# text = ''
# a = input()
# while a != '':
#     text+=a
#     a = input()


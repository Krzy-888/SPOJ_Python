# https://pl.spoj.com/problems/WI_SZYFR/

def Szyfrowanie(character_nubmer, nubmer):
    new_character_number = character_nubmer + nubmer
    if new_character_number > 90:
        new_character_number = new_character_number - 26
    return new_character_number

def Deszyfrowanie(character_nubmer, nubmer):
    new_character_number = character_nubmer - nubmer
    if new_character_number < 65:
        new_character_number = new_character_number + 26
    return new_character_number

def extendCode(characterslengdht,code):
    iterations = int(round(characterslengdht/len(code),0))
    if iterations > characterslengdht/len(code):
        code = code*iterations
    else:
        code = code*(iterations+1)
    return code

def Cezar(mode, text, code):
    try:
        int(code)
    except:
        return "Wrong Data Type, possibele type Integer list without spaces"
    if len(text) > len(code):
        code = extendCode(len(text), code)
    text_list = list(map(ord, text))
    number_list = list(map(int,code))
    if mode == "SZYFRUJ":
        text_list = list(map(Szyfrowanie, text_list,number_list))
        return "".join(list(map(chr, text_list)))
    elif mode == "DESZYFRUJ":
        text_list = list(map(Deszyfrowanie, text_list,number_list))
        return "".join(list(map(chr, text_list)))
    else:
        return "wrong Mode, possible values: SZYFRUJ or DESZYFRUJ"

# print(Cezar("SZYFRUJ", "ZZZZZZZZZZ", "111112"))
# print(Cezar("DESZYFRUJ", "AAAA", "111112"))
# print(Cezar("DESZYFRUJ", "AAAA", "ZWH"))
# print(Cezar("XD", "AAAA", "111112"))
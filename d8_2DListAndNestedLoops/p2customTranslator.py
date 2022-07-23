# Giraffe Language:
# vowels -> g
# -----------------
#
# eg:-
# dog -> dgg
# cat -> cgt

def is_vowel(alphabet):
    if alphabet == 'a' or alphabet == 'e' or alphabet == 'i' or alphabet == 'o' or alphabet == 'u' \
            or alphabet == 'A' or alphabet == 'E' or alphabet == 'I' or alphabet == 'O' or alphabet == 'U':
        return True
    return False


def custom_translator(sentence):
    ans = ''
    for index in range(len(sentence)):
        if is_vowel(sentence[index]):
            if 'A' <= sentence[index] <= 'Z':
                ans += 'G'
            else:
                ans += 'g'
        else:
            ans += sentence[index]
    return ans


if __name__ == '__main__':
    line = input('Enter a sentence: ')
    print(custom_translator(line))

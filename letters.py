import string


def letter_count(file):
    counter = {}
    text = open(file, 'r')
    content = text.read()
    text.close()
    for characters in string.ascii_lowercase:
        counter[characters] = content.count(characters)
    return counter


counter = (letter_count("frost.txt"))
print(counter)


def letter_frequency(dict_letters):
    frequency = {}
    lettercount = 0
    for key in dict_letters:
        lettercount += dict_letters[key]
    for key in dict_letters:
        current_total = dict_letters[key]/lettercount
        frequency[key] = current_total
    return frequency


print(letter_frequency(counter))

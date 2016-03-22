import re

def abbreviate(string):
    Acronym = ''

    for word in re.split(u'[ -]+', string):
        if word.isupper() or word.islower():
            Acronym += word[0]
        else:
            for char in word:
                if char.isupper():
                    Acronym += char

    return Acronym.upper()

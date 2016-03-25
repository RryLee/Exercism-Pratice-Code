def translate(word):
    if word[0].lower() in "aeiou":
        return word + 'ay'
    else:
        while word[0].lower() not in "aeiou":
            word = word[1::] + word[0]
        return word + 'ay'

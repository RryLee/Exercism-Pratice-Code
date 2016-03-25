def hey(what):
    this = what.strip() # badly named variables are fun
    if not this:
        return 'Fine. Be that way!'
    elif this.isupper():
        return 'Whoa, chill out!'
    elif this.endswith('?'):
        return 'Sure.'
    else:
        return 'Whatever.'

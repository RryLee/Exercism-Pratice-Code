from collections import Counter

def detect_anagrams(obj, lists):
    return filter(lambda x: x.lower() != obj.lower() and Counter(x.lower()) == Counter(obj.lower()), lists)

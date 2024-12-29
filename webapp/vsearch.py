def search4vowels(word:str) -> set :
    """Display any vowels found in supplied word"""
    vowels = set("aeiou")
    found = vowels.intersection(set(word))
    for vowel in found:
        print(vowel)
        
def search4letters(phrase:str, letters:str='aeiou') -> set:
    """Returns a set of letters in the phrase"""
    return set(letters).intersection(set(phrase))

search4letters("hello","efg")

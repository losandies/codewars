def disemvowel(str):
    vowels = "aeoiuAEIOU"
    new_string = ""
    for letter in str:
        if letter not in vowels:
            new_string += letter
    return new_string


disemvowel("My gym partner is a monkey")

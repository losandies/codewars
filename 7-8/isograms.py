def is_isogram(s):
    string = s.lower()

    if len(string) == len(set(string)):
        return True
    return False

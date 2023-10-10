def filter_list(l):
    "return a new list with the strings filtered out"
    return [x for x in l if not isinstance(x, str)]


# Most Clever
# def filter_list(l):
#   'return a new list with the strings filtered out'
#   return [i for i in l if not isinstance(i, str)]

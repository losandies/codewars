def high_and_low(numbers):
    ints = []
    for num in numbers.split(" "):
        ints.append(int(num))
    return f"{max(ints), min(ints)}"


# Voted Most Clever:
# def high_and_low(numbers): #z.
#     nn = [int(s) for s in numbers.split(" ")]
#     return "%i %i" % (max(nn),min(nn))

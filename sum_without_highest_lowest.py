def sum_array(arr):
    # your code here
    if not arr or len(arr) < 3:
        return 0

    new_array = sorted(arr)

    return sum(
        x for ind, x in enumerate(new_array) if ind != 0 and ind != len(new_array) - 1
    )


# Most Clever
# def sum_array(arr):
#     return sum(sorted(arr)[1:-1]) if arr and len(arr) > 1 else 0

def get_permutations(square_height):
    if square_height < 1:
        return 0
    if square_height == 1:
        return 2
    if square_height == 2:
        return 6

    # All paths with changes in only the rightmost column.
    total = square_height + 1
    # This is the first permutation set. Calculate all paths involving changes
    # in the two rightmost columns.
    permutations = [i for i in reversed(range(total))][:-1]

    # Using the first permutation set as a tail, calculate all paths involving
    # changes with the already calculated columns, and the next left-most column.
    #
    # subtract 2 because we exclude the right border case, and the first permutation set.
    for i in range(square_height - 2):
        permutations = [sum(permutations[i:]) for i in range(len(permutations))]

    # Multiply by 2 because we only need to brute force the top triangle/half.
    # TODO: optimize the brute force by only calculating half the permutations
    # EVERY time we hit a square and multiplying by 2.
    return sum(permutations) * 2

print get_permutations(20)

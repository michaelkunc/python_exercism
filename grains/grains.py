def on_square(square_number):
    return 2 ** (square_number - 1)


def total_after(square_number):
    total = 0
    for i in range(1, square_number + 1):
        total += on_square(i)
    return total

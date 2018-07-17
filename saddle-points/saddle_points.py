def saddle_points(matrix):
    pass


def get_cols(matrix):
    return [[l[i] for l in matrix] for i in range(0,3)]


def get_rows(matrix):
    return [[l[i] for i in range(0, 3)] for l in matrix]


def max_val(rows):
    return [max(row) for row in rows]


def min_val(columns):
    return [min(col) for col in columns]

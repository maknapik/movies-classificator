def filter_column_by_regex(data, column, regex):
    return data[data[column].str.contains(regex) == True]


def round_column_by_digits(column, digits):
    return column.map(lambda x: round(x, digits))


def column_values_to_int(column):
    return column.map(lambda x: int(x))
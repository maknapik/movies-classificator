def filter_column_by_regex(data, column, regex):
    return data[data[column].astype(str).str.contains(regex) == True]


def filter_column_by_empty_list_of_genres(data):
    return data[data['genres'].apply(lambda x: 'id' in x and 'name' in x)]


def get_genres_names(genres_list):
    return list(map(lambda x: x['name'], genres_list))


def round_column_by_digits(column, digits):
    return column.map(lambda x: round(x, digits))


def column_values_to_int(column):
    return column.map(lambda x: int(x))

from pandas import *
from datetime import *
from operation.data_prepare import *

from configuration.CONSTANTS import *


def get_credits():
    return pandas.read_csv(CREDITS_PATH)


def get_keywords():
    return pandas.read_csv(KEYWORDS_PATH)


def get_movies_metadata():
    data = pandas.read_csv(MOVIES_METADATA_PATH)
    data = data.filter(items=['id', 'title', 'popularity', 'release_date', 'genres', 'budget', 'revenue'])

    data = filter_column_by_regex(data, 'id', '^[0-9]+$')
    data = filter_column_by_regex(data, 'popularity', '^[1-9]+(.[0-9]+)?$')
    data['popularity'] = pandas.to_numeric(data['popularity'])
    data['popularity'] = column_values_to_int(data['popularity'])

    data['income'] = pandas.to_numeric(data['revenue']) - pandas.to_numeric(data['budget'])

    data = filter_column_by_regex(data, 'release_date', '^[0-9]{4}-[0-9]{2}-[0-9]{2}$')
    data['release_date'] = data['release_date'].map(lambda date : datetime.strptime(date, '%Y-%m-%d').month)

    data = filter_column_by_empty_list_of_genres(data)
    data['genres'] = get_genres(data)

    return data.drop(columns=['budget', 'revenue'])


def get_genres(data):
    return data['genres'].map(lambda x: get_genres_names(ast.literal_eval(x)))


def get_genres_unique(data):
    return pandas.unique(pandas.DataFrame(data['genres'].tolist(), index=data['id'])
                         .stack()
                         .reset_index(level=1, drop=True)
                         .reset_index(name='genres')['genres'])


def get_ratings():
    data = pandas.read_csv(RATINGS_PATH)
    data = data.filter(items=['movieId', 'rating'])

    data = data.groupby(['movieId']).mean()
    data['rating'] = round_column_by_digits(data['rating'], 1)

    return data

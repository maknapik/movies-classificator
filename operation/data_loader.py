from pandas import *
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

    return data.drop(columns=['budget', 'revenue'])


def get_ratings():
    data = pandas.read_csv(RATINGS_PATH)
    data = data.filter(items=['movieId', 'rating'])

    data = data.groupby(['movieId']).mean()
    data['rating'] = round_column_by_digits(data['rating'], 1)

    return data

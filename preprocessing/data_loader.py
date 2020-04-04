from pandas import *
from datetime import *
import ast
from sklearn.preprocessing import MinMaxScaler
import numpy

from preprocessing.data_prepare import *
from configuration.CONSTANTS import *


def get_credits():
    return pandas.read_csv(CREDITS_PATH)#.to_dict()


def get_keywords():
    return pandas.read_csv(KEYWORDS_PATH)


def get_movies_metadata():
    data = pandas.read_csv(MOVIES_METADATA_PATH)
    data = data.filter(
        items=['id', 'title', 'popularity', 'release_date', 'genres', 'budget', 'revenue', 'vote_average',
               'vote_count'])

    data = filter_column_by_regex(data, 'id', '^[0-9]+$')
    data['id'] = pandas.to_numeric(data['id'])

    data = filter_column_by_regex(data, 'popularity', '^[0-9]+(.[0-9]+)?$')
    data['popularity'] = pandas.to_numeric(data['popularity'])
    data['popularity'] = column_values_to_int(data['popularity'])

    data['income'] = pandas.to_numeric(data['revenue']) - pandas.to_numeric(data['budget'])

    data = filter_column_by_regex(data, 'release_date', '^[0-9]{4}-[0-9]{2}-[0-9]{2}$')
    data['release_date'] = data['release_date'].map(lambda date: datetime.strptime(date, '%Y-%m-%d').month)

    data = filter_column_by_empty_list_of_genres(data)
    data['genres'] = get_json_genres(data)

    data['vote_count'] = column_values_to_int(data['vote_count'])

    scale_movies_metadata_values(data)

    return data.drop(columns=['budget', 'revenue'])


def get_json_genres(data):
    return data['genres'].map(lambda x: get_genres_names(ast.literal_eval(x)))


def scale_movies_metadata_values(data):
    popularity_scaler = MinMaxScaler(feature_range=(0, POPULARITY_MAX))
    data['popularity'] = popularity_scaler.fit_transform(data[['popularity']])

    income_scaler = MinMaxScaler(feature_range=(0, INCOME_MAX))
    data['income'] = income_scaler.fit_transform(data[['income']])

    vote_count_scaler = MinMaxScaler(feature_range=(0, VC_MAX))
    data['vote_count'] = vote_count_scaler.fit_transform(data[['vote_count']])


def get_movies_ids(data):
    return data['id'].tolist()


def get_flatten_genres(data):
    return pandas.DataFrame(data['genres'].tolist(), index=data['id']) \
        .stack() \
        .reset_index(level=1, drop=True) \
        .reset_index(name='genres')['genres']


def get_genres_unique(data):
    return pandas.unique(get_flatten_genres(data))


def get_ratings(movies_ids):
    data = pandas.read_csv(RATINGS_PATH)
    data = data.filter(items=['movieId', 'rating'])

    data = data.groupby('movieId', as_index=False)['rating'].mean()
    data['rating'] = round_column_by_digits(data['rating'], 1)

    return data[data['movieId'].apply(lambda id: id in movies_ids)]


def join_movies_metadata_and_ratings(data, ratings):
    return data.join(ratings.set_index('movieId'), on='id')


def count_success_factors(data):
    data['success_factor'] = count_success_factor(data['popularity'], data['income'], data['rating'],
                                                  data['vote_average'], data['vote_count'])


def count_success_factor(popularity, income, rating, vote_average, vote_count):
    return count_attribute_factor(POPULARITY_MAX, ALFA) * popularity \
           + count_attribute_factor(INCOME_MAX, BETA) * income \
           + count_attribute_factor(RATING_MAX, GAMMA) * rating \
           + count_attribute_factor(VA_MAX * VC_MAX, DELTA) * vote_average * vote_count


def count_attribute_factor(max, contribution):
    return SUCCESS_FACTOR_MAX * contribution / max


def get_data_with_flatten_genres(data):
    return data.explode('genres')


def save_movies_metadata_with_success_factor_to_file(data):
    data.to_csv(MOVIES_METADATA_WITH_SUCCESS_FACTOR_GENERATED, index=False)


def get_movies_metadata_with_success_factor():
    data = pandas.read_csv(MOVIES_METADATA_WITH_SUCCESS_FACTOR_GENERATED)

    data['genres'] = data['genres'].map(lambda x: ast.literal_eval(x))

    return data

# credits
def prepare_credits_features(data):
    
    data['cast'] = list(map(lambda x: get_essential_features(ast.literal_eval(x), 'character', 'name'), data['cast']))
    data['crew'] = list(map(lambda x: get_essential_features(ast.literal_eval(x), 'job', 'name'), data['crew']))
    data['id'] =  column_values_to_int(data['id'])

    return data

def get_essential_features(feature_data, *args):
    new_feat_data = []

    for dict_elem in feature_data:
        new_dict_elem = {}
        for field in args:
            new_dict_elem[field] = dict_elem[field]
        new_feat_data.append(new_dict_elem)
    return new_feat_data    

""" empty_credits contains ids of rows which have empty cast and crew columns"""
def get_processed_credits(data, empty_credits):
    data = data[data['id'].apply(lambda x: x not in empty_credits)]
    return data
    
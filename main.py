from preprocessing.data_loader import *
from preprocessing.data_prepare import *
from analysis.data_analysis import *

from numpy import asarray
from pandas import *
import matplotlib.pyplot as plt
import ast
from preprocessing import data_loader as dl
from preprocessing.data_prepare import *

def main():
    pandas.set_option('display.max_rows', None)
    pandas.set_option('display.max_columns', None)
    pandas.set_option('display.width', None)
    pandas.set_option('display.max_colwidth', None)

    # data = get_movies_metadata()

    # print(data['vote_count'].sort_values(ascending=False).tail(180))
    #
    # show_column_statistics(data['vote_average'])
    # show_column_statistics(data['vote_count'])

    # plt.hist(ratings['rating'], 10, facecolor='blue', alpha=1)
    # plt.title('Rating histogram')
    # plt.ylabel('amount')
    # plt.xlabel('rating')
    # plt.show()

    # print(data.sort_values(by='income', ascending=True)[['title', 'income', 'genres']].head(10))

    # print(data['popularity'].sort_values(ascending=True).head(100))
    # print(data['popularity'].min())
    #     # print(data['popularity'].max())
    #     # print(data[data['popularity'] == 0]['popularity'].count())
    # print(data['income'].sort_values(ascending=False).head(10))
    # show_genres_histogram(data)

    # ratings = get_ratings(get_movies_ids(data))
    # print(ratings['movieId'])
    # show_column_statistics(ratings['movieId'])
    # show_column_statistics(ratings['rating'])

    # show_vote_count_histogram(data)

    # data = join_movies_metadata_and_ratings(data, ratings)
    # count_success_factors(data)

    # print(data['success_factor'].sort_values(ascending=True).head(100))

    #data = get_movies_metadata_with_success_factor()
    # print(data[data['release_date'] == 10].sort_values(by='success_factor', ascending=False)[
    #           ['title', 'success_factor', 'genres']].head(20))
    # print(data.columns)
    # print(get_genres_unique(data))
    # print(get_data_with_flatten_genres(data[data['release_date'] == 10]).sort_values(by='success_factor', ascending=False).head(20))
    # save_movies_metadata_with_success_factor_to_file(data)
    #print(get_best_genres_by_month(data, 3).sort_values(by='popularity', ascending=False))

    #show_genres_by_month_histogram(data, 3)

    credits = dl.get_credits()
    data = dl.prepare_credits_features(credits)
    counter = 0
    count_empty = 0
    empty_list = filter_empty_movie_credits(data)
        

if __name__ == '__main__':
    main()

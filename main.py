from preprocessing.data_loader import *
from preprocessing.data_prepare import *
from analysis.data_analysis import *
from user_interface.request_handler import handle_request

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

    # data = get_movies_metadata_with_ratings()
    # count_success_factors(data)

    # print(data['success_factor'].sort_values(ascending=True).head(100))

    # data = get_movies_metadata_with_success_factor()
    # print(data[data['release_date'] == 10].sort_values(by='success_factor', ascending=False)[
    #           ['title', 'success_factor', 'genres']].head(20))
    # print(data.columns)
    # print(get_genres_unique(data))
    # print(get_data_with_flatten_genres(data[data['release_date'] == 10]).sort_values(by='rating', ascending=False).head(20))
    # save_movies_metadata_with_success_factor_to_file(data)
    # print(get_best_genres_by_month(data, 3).sort_values(by='popularity', ascending=False))

    # show_genres_by_month_histogram(data, 3)

    # credits = dl.get_credits()
    # data = dl.prepare_credits_features(credits)
    # empty_list = filter_empty_movie_credits(data)
    # data = dl.get_processed_credits(data, empty_list)
    
    # dl.save_processed_credits_to_file(data)

    # res1 = count_workers_by_gender(data, 'cast')
    # res2 = count_workers_by_gender(data, 'crew')
    # print("COUNT CAST MEN = {} and WOMEN = {} and NOT_DEFINED = {}".format(res1[0], res1[1], res1[2]))
    # print("COUNT CREW MEN = {} and WOMEN = {} and NOT_DEFINED = {}".format(res2[0], res2[1], res2[2]))
    # show_credits_people_by_gender([res1[0], res1[1], res1[2]], "cast_gender.png")
    # show_credits_people_by_gender([res2[0], res2[1], res2[2]], "crew_gender.png")
    # data = get_movies_metadata_with_success_factor()
    # show_heat_map(data.drop(columns=['id']))
    # factor = reduction_for_movies_metadata_with_ratings(get_movies_metadata_with_ratings(), 10, 'tsne', 3)
    # print(factor)
    # pca_for_movies_metadata_with_ratings(get_movies_metadata_with_ratings())

    # best_genres = dl.get_best_genres_for_actor("Tom Hanks")
    # print(best_genres)
    # handle_request()
    dl.get_best_actors_group_for_genre("Drama")
    #dl.get_top_movies_in_genre("Drama")


if __name__ == '__main__':
    main()

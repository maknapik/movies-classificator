from preprocessing.data_loader import *

import matplotlib.pyplot as plt


def show_column_statistics(column):
    print("Count: {}".format(column.count()))
    print("Min: {}".format(column.min()))
    print("Mean: {}".format(column.mean()))
    print("Max: {}".format(column.max()))


def show_popularity_histogram(data):
    popularity = data['popularity']

    plt.hist(popularity, 75, facecolor='blue', alpha=1)
    plt.title('Popularity histogram')
    plt.ylabel('amount')
    plt.xlabel('popularity')
    plt.show()


def show_vote_average_histogram(data):
    popularity = data['vote_average']

    plt.hist(popularity, 20, facecolor='blue', alpha=1)
    plt.title('Vote average histogram')
    plt.ylabel('amount')
    plt.xlabel('vote average')
    plt.show()


def show_vote_count_histogram(data):
    popularity = data['vote_count']

    plt.hist(popularity, 20, facecolor='blue', alpha=1)
    plt.title('Vote count histogram')
    plt.ylabel('amount')
    plt.xlabel('vote count')
    plt.show()


def show_genres_histogram(data):
    genres = get_flatten_genres(data)

    plt.hist(genres, 20, facecolor='blue', alpha=1)
    plt.title('Genres histogram')
    plt.ylabel('amount')
    plt.xlabel('genre')
    plt.show()


def show_success_factor_histogram(data):
    success_factor = data['success_factor']

    plt.hist(success_factor, 100, facecolor='blue', alpha=1)
    plt.title('Success factor histogram')
    plt.ylabel('amount')
    plt.xlabel('success factor')
    plt.show()

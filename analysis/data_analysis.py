from preprocessing.data_loader import *

import matplotlib.pyplot as plt
import seaborn as sns
import pandas


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


def get_best_genres_by_month(data, month):
    data = get_best_flatten_genres_by_month(data, month)

    data = data.groupby('genres', as_index=False).count()[['genres', 'popularity']]

    return data


def get_best_flatten_genres_by_month(data, month):
    return get_data_with_flatten_genres(data[data['release_date'] == month]) \
        .sort_values(by='success_factor', ascending=False) \
        .head(BEST_GENRES_BY_MOVIES_TAKEN_POSITIONS)


def show_genres_by_month_histogram(data, month):
    genres = get_best_flatten_genres_by_month(data, month)['genres']

    plt.hist(genres, pandas.unique(genres), facecolor='blue', alpha=1)
    plt.title('Genres histogram')
    plt.suptitle('For month: {}'.format(month))
    plt.ylabel('amount')
    plt.xlabel('genre')
    plt.show()


# credits
def show_credits_people_by_gender(genders_appearance, file_name):
    data = ["Man", "Woman", "Not_defined"]
    gender_types = numpy.arange(len(data))
    plt.bar(gender_types, genders_appearance, align='center', alpha=0.5)
    plt.title('Genders histogram')
    plt.xticks(gender_types, data)
    plt.ylabel('amount')
    plt.xlabel('gender')
    for i, d in enumerate(genders_appearance):
        plt.text(x=i, y=d, s=str(d), horizontalalignment='center')
    plt.savefig(file_name)


def show_heat_map(data):
    colormap = plt.cm.viridis
    plt.figure(figsize=(12, 12))
    plt.title('Pearson Correlation of Features', y=1.05, size=15)
    sns.heatmap(data.astype(float).corr(), linewidths=0.1, vmax=1.0, square=True, cmap=colormap, linecolor='white',
                annot=True)
    plt.show()

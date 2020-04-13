from preprocessing.data_loader import *

import matplotlib.pyplot as plt
import seaborn as sns
import pandas
import random
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA


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

    return data.sort_values(by='popularity', ascending=False)


def get_best_flatten_genres_by_month(data, month):
    return get_data_with_flatten_genres(data[data['release_date'] == month]) \
        .sort_values(by='success_factor', ascending=False) \
        .head(BEST_GENRES_BY_MONTHS_TAKEN_POSITIONS)


def show_genres_by_month_histogram(data, month):
    genres = get_best_flatten_genres_by_month(data, month)['genres']

    plt.hist(genres, pandas.unique(genres), facecolor='blue', alpha=1)
    plt.title('Genres histogram')
    plt.suptitle('For month: {}'.format(MONTHS_IDS.get(month)))
    plt.ylabel('amount')
    plt.xlabel('genre')
    plt.show()


def pca_for_movies_metadata_with_ratings(data):
    features = ['popularity', 'vote_average', 'vote_count', 'income', 'rating']
    f_data = data[features]
    f_data = StandardScaler().fit_transform(f_data)

    pca = PCA(n_components=2)
    principal_components = pca.fit_transform(f_data)
    principal_df = pandas.DataFrame(data=principal_components,
                                    columns=['principal component 1', 'principal component 2'])

    final_df = get_data_with_flatten_genres(pandas.concat([principal_df, data[['id', 'title', 'genres']]], axis=1))

    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(1, 1, 1)
    ax.set_xlabel('Principal Component 1', fontsize=15)
    ax.set_ylabel('Principal Component 2', fontsize=15)
    ax.set_title('2 component PCA', fontsize=20)
    targets = get_genres_unique(data)
    colors = [get_random_color() for x in range(len(targets))]
    for target, color in zip(targets, colors):
        indices_to_keep = final_df['genres'] == target
        ax.scatter(final_df.loc[indices_to_keep, 'principal component 1']
                   , final_df.loc[indices_to_keep, 'principal component 2']
                   , c=color
                   , s=50)
    ax.legend(targets)
    ax.grid()
    plt.show()


def get_random_color():
    random_number = random.randint(1118481, 16777215)
    hex_number = str(hex(random_number))
    return '#' + hex_number[2:]


def get_months_by_genre(genre):
    data = get_movies_metadata_with_success_factor()
    indices = []
    for month in range(1, 13):
        best = get_best_genres_by_month(data, month)
        try:
            indices.append(best['genres'].tolist().index(genre))
        except ValueError:
            indices.append(len(get_genres_unique(data)))

    best = pandas.DataFrame({'month': list(MONTHS_IDS.values()), 'rank': indices})
    best['rank'] = best['rank'].map(lambda x: x + 1)
    return best


def show_months_histogram_by_genre(genre):
    data = get_months_by_genre(genre)
    data['rank'] = data['rank'].map(lambda x: 1/x)

    fig, ax = plt.subplots(nrows=1, ncols=1)
    ax.bar(data['month'], data['rank'])
    plt.title('Months histogram')
    plt.suptitle('For genre: {}'.format(genre))
    plt.ylabel('factor')
    plt.xlabel('month')
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

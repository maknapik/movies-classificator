import argparse
from preprocessing.data_loader import *
from analysis.data_analysis import *


def show_available_genres():
    data = get_movies_metadata()
    print(get_genres_unique(data))


def show_genres_by_month(month):
    data = get_movies_metadata_with_success_factor()
    print(get_best_genres_by_month(data, int(month)).sort_values(by='popularity', ascending=False))


def show_genres_histogram_by_month(month):
    data = get_movies_metadata_with_success_factor()
    show_genres_by_month_histogram(data, int(month))


def handle_request():
    parser = argparse.ArgumentParser(description='Movies and Actors Classification System (MACS)')
    parser.add_argument('-sg', help='Show list of available genres', action='store_true')
    parser.add_argument('-g', metavar='N', nargs=1, help='Show list of most accurate genres for given month',
                        type=show_genres_by_month)
    parser.add_argument('-gh', metavar='N', nargs=1, help='Show histogram of most accurate genres for given month',
                        type=show_genres_histogram_by_month)

    args = parser.parse_args()

    if args.sg:
        show_available_genres()

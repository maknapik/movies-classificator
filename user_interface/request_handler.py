import argparse
from preprocessing.data_loader import *
from analysis.data_analysis import *


def show_available_genres():
    data = get_movies_metadata()
    print(get_genres_unique(data))


def show_genres_by_month(month):
    data = get_movies_metadata_with_success_factor()
    print(get_best_genres_by_month(data, int(month)))


def show_genres_plot_by_month(month):
    data = get_movies_metadata_with_success_factor()
    show_genres_by_month_histogram(data, int(month))


def show_months_by_genre(genre):
    print(get_months_by_genre(genre).sort_values(by='rank', ascending=True).head(BEST_MONTHS_BY_GENRES_TAKEN_POSITIONS))


def show_best_genres_for_actor(actor):
    best_genres = get_best_genres_for_actor(actor)
    print(best_genres) if best_genres is not None else print("Such actor does not exist in movies database")


def show_best_movies_for_genre(genre):
    top_movies_in_genre = get_top_movies_in_genre(genre)
    print(top_movies_in_genre) if len(top_movies_in_genre) != 0 else print("Such genre does not exist in movies database")


def show_best_actors_group_for_genre(genre, exploreMore=False):
    best_actors_group_in_genre = get_best_actors_group_for_genre(genre, exploreMore)
    print(best_actors_group_in_genre) if len(best_actors_group_in_genre) != 0 \
                                      else print("Can not find best actors group in movies database")    


class CustomAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        data = get_movies_metadata_with_ratings()
        reduction_for_movies_metadata_with_ratings(data, int(values[0]), values[1], int(values[2]))


def handle_request():
    parser = argparse.ArgumentParser(description='Movies and Actors Classification System (MACS)')
    parser.add_argument('-sg', help='Show list of available genres', action='store_true')
    parser.add_argument('-m', metavar='month', nargs=1, help='Show list of most accurate genres for given month',
                        type=show_genres_by_month)
    parser.add_argument('-mh', metavar='month', nargs=1, help='Show bar plot of most accurate genres for given month',
                        type=show_genres_plot_by_month)
    parser.add_argument('-g', metavar='genre', nargs=1, help='Show list of most accurate months for given genre',
                        type=show_months_by_genre)
    parser.add_argument('-gh', metavar='genre', nargs=1, help='Show plot of most accurate months for given genre',
                        type=show_months_histogram_by_genre)
    parser.add_argument('-agn', metavar='actor', nargs=1, help='Show list of most accurate movie genres for given actor',
                        type=show_best_genres_for_actor)
    parser.add_argument('-rd', metavar=('month', 'method', 'dim'), nargs=3,
                        help='Show 2D or 3D plot with reduced data. Method: pca|tsne. Dim: 2|3',
                        action=CustomAction)
    parser.add_argument('-hm', help='Show heat-map of movies\' features', action='store_true')
    parser.add_argument('-bgm', metavar='genre', nargs=1, help='Show list of best movies for given genre',
                        type=show_best_movies_for_genre)
    parser.add_argument('-agg', nargs=1, help='Show list of actors group for given genre',
                        action='store')
    parser.add_argument('--exploreMore', help='Conduct more detailed exploration of best actors group for genre',
                         action='store_true')                    

    args = parser.parse_args()

    if args.sg:
        show_available_genres()
    if args.hm:
        show_heat_map(get_movies_metadata_with_success_factor().drop(columns=['id', 'title', 'genres']))
    if args.agg and args.exploreMore:
        show_best_actors_group_for_genre(args.agg[0], True)
    if args.agg and not args.exploreMore:
        show_best_actors_group_for_genre(args.agg[0])

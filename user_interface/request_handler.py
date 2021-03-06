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


def show_best_genres_for_months():
    data = get_movies_metadata_with_success_factor()
    print("The best genres for each month")
    for (month, genre) in get_best_genres_for_months(data):
        print("{}: {}".format(month, genre))


def show_best_months_for_genres():
    data = get_movies_metadata_with_success_factor()
    print("The best months for each genre")
    for (genre, month) in get_best_months_for_genres(data):
        print("{}: {}".format(genre, month))


def show_best_genres_for_actor(actor):
    best_genres = get_best_genres_for_actor(actor)
    show_best_genres_for_actor_pie(best_genres, actor, "top_genr.png") if best_genres is not None \
        else print("Such actor does not exist in movies database")


def show_best_movies_for_genre(genre):
    top_movies_in_genre = get_top_movies_in_genre(genre)
    show_best_movies_for_genre_pie(top_movies_in_genre, genre, "top_mov.png") if len(top_movies_in_genre) != 0 \
        else print("Such genre does not exist in movies database")


def show_best_actors_group_for_genre(genre, exploreMore=False):
    best_actors_group_in_genre = get_best_actors_group_for_genre(genre, exploreMore)
    show_summary_for_best_actors_group(best_actors_group_in_genre, exploreMore) if len(best_actors_group_in_genre) != 0 \
        else print("Can not find best actors group in movies database")


class CustomAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        data = get_movies_metadata_with_ratings()
        reduction_for_movies_metadata_with_ratings(data, int(values[0]), values[1], int(values[2]))


def handle_request():
    parser = argparse.ArgumentParser(description='Movies and Actors Classification System (MACS)')
    parser.add_argument('-sg', help='Show list of available genres', action='store_true')
    parser.add_argument('-m', metavar='month', nargs=1, help='Show list of the most accurate genres for given month',
                        type=show_genres_by_month)
    parser.add_argument('-mh', metavar='month', nargs=1,
                        help='Show bar plot of the most accurate genres for given month',
                        type=show_genres_plot_by_month)
    parser.add_argument('-g', metavar='genre', nargs=1, help='Show list of the most accurate months for given genre',
                        type=show_months_by_genre)
    parser.add_argument('-gh', metavar='genre', nargs=1, help='Show plot of the most accurate months for given genre',
                        type=show_months_histogram_by_genre)
    parser.add_argument('-bg', help='Show list of the best genres for each month',
                        action='store_true')
    parser.add_argument('-bm', help='Show list of the best months for each genre',
                        action='store_true')
    parser.add_argument('-agn', metavar='actor', nargs=1,
                        help='Show list of the most accurate movie genres for given actor',
                        type=show_best_genres_for_actor)
    parser.add_argument('-rd', metavar=('month', 'method', 'dim'), nargs=3,
                        help='Show 2D or 3D plot with reduced data. Method: pca|tsne. Dim: 2|3',
                        action=CustomAction)
    parser.add_argument('-hm', help='Show heat-map of movies\' features', action='store_true')
    parser.add_argument('-bgm', metavar='genre', nargs=1, help='Show list of the best movies for given genre',
                        type=show_best_movies_for_genre)
    parser.add_argument('-agg', metavar='genre', nargs=1, help='Show list of actors group for given genre',
                        action='store')
    parser.add_argument('--exploreMore', help='Conduct more detailed exploration of the best actors group for genre',
                        action='store_true')

    args = parser.parse_args()

    if args.sg:
        show_available_genres()
    elif args.bg:
        show_best_genres_for_months()
    elif args.bm:
        show_best_months_for_genres()
    elif args.hm:
        show_heat_map(get_movies_metadata_with_success_factor().drop(columns=['id', 'title', 'genres']))
    elif args.agg and args.exploreMore:
        show_best_actors_group_for_genre(args.agg[0], True)
    elif args.agg and not args.exploreMore:
        show_best_actors_group_for_genre(args.agg[0])

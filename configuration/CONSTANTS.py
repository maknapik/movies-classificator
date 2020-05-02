# file paths
CREDITS_PATH = "data/credits.csv"
KEYWORDS_PATH = "data/keywords.csv"
MOVIES_METADATA_PATH = "data/movies_metadata.csv"
RATINGS_PATH = "data/ratings_new.csv"

GENERATED_DATA_SUFFIX = "generated_data/"
MOVIES_METADATA_WITH_SUCCESS_FACTOR_GENERATED = "generated_data/movies_metadata_with_success_factor.csv"
MOVIES_METADATA_WITH_RATINGS_GENERATED = "generated_data/movies_metadata_with_ratings.csv"
CREDITS_GENERATED = "generated_data/credits_generated.csv"

# success_factor values
SUCCESS_FACTOR_MAX = 100

POPULARITY_MAX = 100
ALFA = 0.10

INCOME_MAX = 100
BETA = 0.10

RATING_MAX = 5
GAMMA = 0.10

VA_MAX = 10  # vote_average max value
VC_MAX = 1000  # vote_count max value
DELTA = 0.70

# analysis constants
# number which indicates how many records should be taken when grouping by genre
BEST_GENRES_BY_MONTHS_TAKEN_POSITIONS = 300
BEST_MONTHS_BY_GENRES_TAKEN_POSITIONS = 20

# constant for selecting how many genres in which actor is specialized should appear in analysis result
MAX_GENRES_ACTOR_SPECIALIZED = 10

MAX_TOP_RATED_MOV_IN_GENRE = 10
MAX_ACTOR_GROUP_SIZE_FROM_MOVIE_FAC = 8
MAX_TOP_GENRES_TO_ADD_ACTOR_TO_GROUP = 2

# additional
MONTHS_IDS = dict(
    {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August", 9: "September",
     10: "October", 11: "November", 12: "December"})

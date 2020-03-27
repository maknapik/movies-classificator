from pandas import *

from configuration.CONSTANTS import *


def get_credits():
    return pandas.read_csv(CREDITS_PATH)


def get_keywords():
    return pandas.read_csv(KEYWORDS_PATH)


def get_movies_metadata():
    return pandas.read_csv(MOVIES_METADATA_PATH, low_memory=False)


def get_ratings():
    return pandas.read_csv(RATINGS_PATH)
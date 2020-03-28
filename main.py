from operation.data_loader import *
from operation.data_prepare import *

import json
from numpy import asarray
from pandas import *
import matplotlib.pyplot as plt
import ast


def main():
    pandas.set_option('display.max_rows', None)
    pandas.set_option('display.max_columns', None)

    data = get_movies_metadata()

    # print(data['genres'].sort_values(ascending=True).tail(180))
    print(get_genres_unique(data))

    # ratings = get_ratings()

    #print(ratings.count())
    # plt.hist(ratings['rating'], 10, facecolor='blue', alpha=1)
    # plt.title('Rating histogram')
    # plt.ylabel('amount')
    # plt.xlabel('rating')
    # plt.show()


if __name__ == '__main__':
    main()

from operation.data_loader import *
from operation.data_prepare import *

from pandas import *
import matplotlib.pyplot as plt


def main():
    pandas.set_option('display.max_rows', None)
    pandas.set_option('display.max_columns', None)

    data = get_movies_metadata()

    # print(data.sort_values(by=['release_date'], ascending=True).head(5))

    ratings = get_ratings()

    plt.hist(ratings['rating'], 75, facecolor='blue', alpha=1)
    plt.show()


if __name__ == '__main__':
    main()

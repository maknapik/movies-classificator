from operation.data_loader import *
from operation.data_prepare import *

from pandas import *
import matplotlib.pyplot as plt


def main():
    pandas.set_option('display.max_rows', None)
    pandas.set_option('display.max_columns', None)

    data = get_movies_metadata().filter(items=['id', 'popularity'])
    data = filter_column_by_regex(data, 'popularity', '^[1-9]+(.[0-9]+)?$')
    data = filter_column_by_regex(data, 'id', '^[0-9]+$')
    data['popularity'] = pandas.to_numeric(data['popularity'])
    data['popularity'] = column_values_to_int(data['popularity'])
    print(data.sort_values(by=['popularity'], ascending=False).tail(45000))
    print(data['popularity'].mean())
    print(len(data['popularity'].unique()))

    plt.hist(data['popularity'], 75, facecolor='blue', alpha=2)
    plt.show()


if __name__ == '__main__':
    main()

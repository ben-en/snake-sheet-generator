# GPL v3.0
# By: Ben Ennis
# URL: https://github.com/ben-en/snake-sheet-generator

# This is a program for generating "snaking" spreadsheets while filtering
# particular fields (coordinates) from being used. With no filter, it would
# generate something like the following:
#   ~# python numbers-to-csv.py 2 5 5 out.csv
#   >>>
#       [2,  '', 12, '', 22]
#       ['', 10, '', 20, '']
#       [4,  '', 14, '', 24]
#       ['',  8, '', 18, '']
#       [6,  '', 16, '', 26]
#       out.csv written!
#
# Help should first and foremost be seen with the '-h' flag, courtesy of
# argparse.


import argparse
import csv
import os
from itertools import zip_longest

import numpy


FILTER = 'filter.csv'


def init_args():
    """ Init args with argparse """
    parser = argparse.ArgumentParser(description='Create xls for Tom')
    parser.add_argument('start', metavar='N', type=int, help='starting '
                        'number')
    parser.add_argument('total_x', metavar='N', type=int,
                        help='total number of x rows')
    parser.add_argument('total_y', metavar='N', type=int,
                        help='total number of y columns')
    parser.add_argument('filename', metavar='NAME', default='test.csv',
                        type=str, help='file name to write to, should end in '
                        'csv')
    parser.add_argument('odd', action='store_true', default=True,
                        help='whether to write odd or even columns')
    return parser.parse_args()


def load_filter():
    """ loads file FILTER, returns filter matrix """
    if not os.path.isfile(FILTER):
        print('no filter found, creating square grid')
        return []
    with open(FILTER, 'r') as ff:
        reader = csv.reader(ff)
        l = list(reader)
        ar = numpy.asarray(l)
        # ar = numpy.transpose(ar, (0, 1))
        # ar = numpy.flip(ar, 1)
        # ar = numpy.rot90(ar, k=3, axes=(0, 1))
        # ar = numpy.swapaxes(ar, 0, 1)
        f = list(map(list, ar))
        return f


def filtered(filter, xy):
    """ returns boolean, whether xy is occupied in filter matrix """
    try:
        x, y = xy
        return bool(filter[x][y])
    except IndexError:
        return False


def create_matrix(totals, filter, start=0, odd=False):
    """ Do all the grunt work of the snaking values, ordering the filtered
    blanks, and basically all the heavy lifting """
    i = start
    blank = ''
    x, y = 0, 0
    total_x, total_y = totals
    # matrix is represented as
    #
    #     row are down
    # t-> 1 7
    #     2 9
    #     3 10
    #     4 11
    #     5 12
    #     6 13

    # Transposed with zip later
    matrix = []
    while y < total_y:
        row = []
        blank_pos = []
        while x < total_x:
            # TODO: Blank all points before starting coords
            if bool(i % 2) and odd:
                row.append(blank)
            elif filtered(filter, (x, y)):
                blank_pos.append(x)
                x += 1
                continue
            else:
                row.append(i)
            x += 1
            i += 1
        if y % 2:  # if odd
            row.reverse()
        for pos in blank_pos:
            row.insert(pos, blank)
        matrix.append(row)
        y += 1
        x = 0
    final = list(map(list, zip_longest(*matrix)))
    print('final matrix')
    for f in final:
        print(f)
    return final


def write_out(matrix, filename):
    """ Write the matrix to a csv table """
    with open(filename, 'w') as csvfile:
        writer = csv.writer(csvfile)
        for r in matrix:
            writer.writerow(r)
    print(filename + ' writen!')


def main():
    args = init_args()
    filter = load_filter()
    matrix = create_matrix((args.total_x, args.total_y), filter, args.start,
                           odd=args.odd)
    write_out(matrix, args.filename)


if __name__ == "__main__":
    main()

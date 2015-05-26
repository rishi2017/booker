__author__ = 'rishirajkalra'

import csv
import os
import httplib2
import random
import string

#current_dir_path = os.getcwd();
filename = "books.csv"
#filepath = os.path.join(os.getcwd(), filename); #filepath to open


def get_file_path(filename):
    file_path = os.path.join(os.getcwd(),filename);
    print(file_path);
    return file_path


path = get_file_path(filename);


def read_csv(filepath):
    isbns = {}
    i=0
    with open(filepath, 'rU') as csvfile:
        reader = csv.reader(csvfile, dialect="excel", delimiter=',')
        for row in reader:
            isbns[i] = row
            i += 1
    print(isbns)
    return isbns


isbn_list = read_csv(path);




#!/usr/bin/env python
#encoding=utf-8
import glob
import os.path

date_format = '%Y-%m-%d'


def file_exists(file_path):
    return os.path.isfile(file_path)


#print file_exists('bandou.db')
#print file_exists('bandou2.db')
#
#print file_exists('cache/test.txt')
#print file_exists('cache/test2.txt')


def find_files(pattern):
    return glob.glob(pattern)


#print find_files('cache/*.txt')
#print find_files('cache/casa_nova_books_*.*')
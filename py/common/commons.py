#!/usr/bin/env python
# coding=utf-8

import glob
import os.path

date_format = '%Y-%m-%d'


def file_exists(file_path):
    return os.path.isfile(file_path)


def find_files(pattern):
    return glob.glob(pattern)

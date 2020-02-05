#!/usr/bin/env python 

import os


def load_files_from_path(path):
    """
    Générateur sur les noms de fichiers titres à partir d'un répertoire.
    :param path:
    :return:
    """
    for file in os.listdir(path):
        yield file


def load_names_from_file(path):
    """
    Générateur sur les noms de fichiers titre à partir d'un fichier.

    :param path:
    :return:
    """
    with open(path) as file:
        for line in file:
            yield line[:-1]


def load_data_from_csv(path, has_header=True):
    # tvshow;season;ep_number;ep_title;duration;year
    with open(path) as csv_file:
        if has_header:
            csv_file.readline()
        for line in csv_file:
            yield line.split(";")


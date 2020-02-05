#!/usr/bin/env python 

import re
import os.path

SE_PATTERN = "-s(?P<season>[0-9]{2})e(?P<episode>[0-9]{2})-"
se_pattern = re.compile(SE_PATTERN)


def extract_from_filename(filename):
    """
    Retourne les informations d'un épisode à partir d'une chaine de caractère
    représentant un fichier.

    :param filename:
    :return: titre série, numéro saison, numéro épisode, titre épisode, extension fichier.
    """
    result = se_pattern.search(filename)
    if result:
        name, ext = os.path.splitext(filename)

        return name[:result.start()].replace('_', ' '), \
               result.group("season"), \
               result.group("episode"), \
               name[result.end():].replace('_', " "), \
               ext

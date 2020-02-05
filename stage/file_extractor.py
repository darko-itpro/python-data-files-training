#!/usr/bin/env python 

import re
import os.path

SE_PATTERN = ""
se_pattern = re.compile(SE_PATTERN)


def extract_from_filename(filename):
    """
    Retourne les informations d'un épisode à partir d'une chaine de caractère
    représentant un fichier.

    :param filename:
    :return: titre série, numéro saison, numéro épisode, titre épisode, extension fichier.
    """
    pass

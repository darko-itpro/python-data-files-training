#!/usr/bin/env python 

import argparse
from data_loader import db_helper
from data_loader import file_helper
from data_loader import file_extractor as extractor
import sqlite3 as sqlite
import os.path

parser = argparse.ArgumentParser(description="Manager for Tv show")

parser.add_argument("command", choices=["load", "display"],
                    help="Action this program should perform")

parser.add_argument("-s", "--show", help="show name should be as string")
parser.add_argument("-n", "--season_number", type=int)
parser.add_argument("-p", "--path")

args = parser.parse_args()

if args.command == "load":
    if args.path:
        if os.path.isdir(args.path):
            for filename in file_helper.load_files_from_path(args.path):
                print(extractor.extract_from_filename(filename))
        elif os.path.splitext(args.path)[1] == ".csv":
            for filename in file_helper.load_data_from_csv(args.path):
                print(filename)
        else:
            for filename in file_helper.load_names_from_file(args.path):
                print(extractor.extract_from_filename(filename))

    else:
        print("Don't know where to look")

elif args.command == "display":
    if args.season_number:
        season = args.season_number
    else:
        season = None

    try:
        data = db_helper.load_episodes(season_number=season, dbname=args.show)
        for title, season, number in data:
            print(f"{title:30} - s{season:02}e{number:02}")
    except sqlite.Error:
        print("erreur de base")

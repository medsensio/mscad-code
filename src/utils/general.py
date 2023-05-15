"""General utility functions."""

import csv
import json
import os


def dump_to_csv(dump_path, long_df, csv_columns):
    """Dump data into csv file.

    Args:
        dump_path (str): path of the csv file to be created
        long_df (list): data to be written in the csv file
        csv_columns (iterable): column names of the csv file
    """
    os.makedirs(os.path.dirname(dump_path), exist_ok=True)
    try:
        with open(dump_path, mode='w', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in long_df:
                writer.writerow(data)
    except IOError:
        print("I/O error")


def read_json_from_file(file_path):
    """Reads a JSON file and returns the JSON object"""
    with open(file_path) as json_file:
        return json.load(json_file)


def dump_json_to_file(file_path, json_string):
    """Dumps a JSON string to a file"""
    with open(file_path, "w") as json_file:
        json_file.write(json_string)


def write_dict_to_json_file(data, file_path):
    """Writes a dictionary to a JSON file"""
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4, sort_keys=False)


def dump_to_markdown(path: str, text: list):
    """Dump data into markdown file."""
    with open(path, mode='w', encoding='utf-8') as f:
        f.write(text)

"""Extract content from XML files and dump it into a single CSV file."""

import glob

from utils.general import dump_to_csv
from utils.xml_processing import obtain_row_dict


XML_FAMILIES = [
    ("raw_data--anonymised/28-11-2022/*/Data/input/*/*.xml", "extracted/horizon.csv"),  # Horizon
    ("raw_data--anonymised/16-03-2022/*/Data/input/*/*.xml", "extracted/sanolla.csv"),  # Sanolla
]


def process_xml_to_csv():
    """This function takes in a set of XML files and converts them to a single CSV file.

    The paths to XML files are expected to be in the format of `xml_path_format`.
    The function iterates through each file and extracts the data contained in each XML tag.
    It then writes this data to a single CSV file stored under `new_csv_dump`.
    """
    for xml_path_format, new_csv_dump in XML_FAMILIES:
        long_df = []
        csv_columns = set()

        all_xml_files = glob.glob(xml_path_format)

        for single_file in all_xml_files:
            long_data_row = obtain_row_dict(single_file)
            long_df.append(long_data_row)
            csv_columns.update(long_data_row.keys())

        dump_to_csv(new_csv_dump, long_df, sorted(csv_columns))


if __name__ == "__main__":
    process_xml_to_csv()

import datetime
import glob
import os

from utils.general import write_dict_to_json_file


# Process only Horizon data
PATH_FORMAT = [
    "raw_data--anonymised/28-11-2022/*/Data/input/*/*/",
    "raw_data--anonymised/16-03-2022/*/Data/input/*/*/",
]


# The order of the auscultation recordings if exactly 10 are provided
RECORDINGS_ORDER = {
    0: "361959008",
    1: "361955002",
    2: "312581008",
    3: "312580009",
    4: "361970001",
    5: "245522000",
    6: "181287002",
    7: "181289004",
    8: "181288007",
    9: "181286006",
}

UNKNOWN_LOCATION = "51185008"


def main():
    """Generate the auscultation locations."""
    # Get encounters directories
    for dataset in PATH_FORMAT:
        directories = glob.glob(dataset)

        for encounter in directories:
            # Generate the list of channel 1 audio recordings
            audio_files = glob.glob(encounter + "*_ch1.wav")
            if audio_files == []:
                continue

            # Get filenames
            audio_files = [os.path.basename(file) for file in audio_files]

            # Generate auscultation locations only if there are exactly 10 recordings
            if len(audio_files) == 10 and "Covid-19" not in encounter:
                file_location = {}
                times = []
                # Extract the time of recording from the filename
                for file in audio_files:
                    hour, minute, second = file.split("_")[0:3]
                    times.append(datetime.time(int(hour), int(minute), int(second)))

                # Sort the recordings by time
                ordered = sorted(enumerate(times), key=lambda x: x[1])
                # Prepare the dictionary: filename -> auscultation location
                for i, (index, _) in enumerate(ordered):
                    file_location[audio_files[index]] = RECORDINGS_ORDER[i]

            # The unknown location points to the "Chest" body structure
            else:
                file_location = {file: UNKNOWN_LOCATION for file in audio_files}

            # Write the dictionary to a JSON file
            locations_path = os.path.join(encounter, "locations.json")
            write_dict_to_json_file(file_location, locations_path)


if __name__ == "__main__":
    main()

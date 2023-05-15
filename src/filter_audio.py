"""Apply filtering to audio files."""

import os
import shutil

import sox

from tqdm import tqdm


SEPARATED_CHANNELS_DIR = "raw_data--anonymised/"
OUTPUT_DIR = "filtered/"

# Set to True to only process channel 1
ONLY_CH1 = True


def process_files():
    """Apply filtering to audio files."""
    # Set up the output directory
    setup_folder()

    # Count the number of files to process
    file_count = sum(len(files) for root, _, files in os.walk(SEPARATED_CHANNELS_DIR) if "input" in root)
    # Set the progress bar
    with tqdm(total=file_count) as pbar:

        # Recursively walk through the raw data directory
        for root, _, files in os.walk(SEPARATED_CHANNELS_DIR):
            # Process only `input` directories
            if "input" not in root:
                continue

            for file in files:
                # Update the progress bar
                pbar.update(1)

                # Skip files which are not WAV files
                if not is_wav(file):
                    continue

                # Skip files which are not channel 1
                if not is_ch1(file):
                    continue

                # Create the source and destination paths
                src_path = os.path.join(root, file)
                dst_path = src_path.replace(
                    SEPARATED_CHANNELS_DIR,
                    OUTPUT_DIR,
                )

                # Create the destination directory if it does not exist
                os.makedirs(os.path.dirname(dst_path), exist_ok=True)

                # Apply filtering
                apply_filter(src_path, dst_path)


def setup_folder():
    """Set up the output directory."""
    # Remove the output directory if it exists
    if os.path.isdir(OUTPUT_DIR):
        shutil.rmtree(OUTPUT_DIR)
    # Create the output directory
    os.mkdir(OUTPUT_DIR)

    # Verify that the output directory was created
    if not os.path.isdir(OUTPUT_DIR):
        raise RuntimeError("Could not create output directory")


def is_wav(filespath):
    """Check if the file is a WAV file."""
    return filespath.endswith(".wav")


def is_ch1(filespath):
    """Check if the file is a channel 1 file."""
    if not ONLY_CH1:
        return True
    return filespath.endswith("_ch1.wav")


def apply_filter(src_path, dst_path):
    """Apply filtering to an audio file."""
    # Create the transformer
    tfm = sox.Transformer()
    # Apply the filter
    tfm.highpass(70)
    tfm.lowpass(800)
    # Apply the transformer
    tfm.build(src_path, dst_path)

if __name__ == "__main__":
    process_files()

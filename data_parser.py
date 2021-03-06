# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a script file to pick up the OGG files from the subfolders and put them in a h5 dataset..
"""

# In[1]:
# Import the packages you need
import sys
import numpy
from helpers import *

OUTPUT_DATASET = "sounddataset.h5"
MINIMUM_NUMBER_OF_FEATURES = 160703
# In[2]:
# Take folder inputs from command line.

def main():
    '''
    '''
    source_folder = "."
    destination_folder = "."
    if len(sys.argv) == 3:
        source_folder = sys.argv[1]
        destination_folder = sys.argv[2]
    else:
        print("Invalid number of arguments. Will use the current folder as source and destination")

    validate_path(source_folder)
    validate_path(destination_folder)

    # In[]
    source_sub_folders = get_subfolders(source_folder)
    print("Getting folders from the directory "+ source_folder)
    print("Found the following sub folders")
    line_number = 1
    for folder in source_sub_folders:
        print(line_number, ". ", folder)
        if line_number > 5:
            print("and more like these ...")
            break
        line_number += 1

    # In[]
    for folder in source_sub_folders:
        print("\nChecking ", folder, ".")
        data_tag = get_data_tag_from_folder_name(folder)
        sound_files_in_this_folder = get_sound_files(folder)
        print("Found ", len(sound_files_in_this_folder), " sound files in this folder.")
        for sound_file in sound_files_in_this_folder:
            print("Analysing the file : ", sound_file)
            features = get_features_from_sound_file(source_folder, folder, sound_file)
            features_list = numpy.array(features)
            features_list = features_list.reshape((-1, 1))
            # Add features to dataset
            if 'dataset' not in locals():
                dataset = features_list[:MINIMUM_NUMBER_OF_FEATURES,:]
            else:
                dataset = np.hstack((dataset, features_list[:MINIMUM_NUMBER_OF_FEATURES,:]))
            # Add tags to dataset
            if 'dataset_y' not in locals():
                dataset_y = np.array([data_tag.encode('utf8') ])
            else:
                dataset_y = np.hstack((dataset_y, [data_tag.encode('utf8') ]))
            print("Added ", sound_file, " to dataset")

    write_dataset_to_file(destination_folder, OUTPUT_DATASET, dataset, dataset_y)


if __name__ == "__main__":
    # execute only if run as a script
    main()
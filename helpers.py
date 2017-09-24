# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 19:38:41 2017

@author: shrung
"""

# In[]
import os
import soundfile as sf
import h5py
import sys
import numpy as np

# In[]
def validate_path(path):
    '''

    '''
    return os.path.isdir(path)

def get_subfolders(path):
    '''
    '''
    all_foiders = os.listdir(path)
    all_foiders = [item for item in all_foiders if item[0] not in [".","_"]]
    all_foiders = [item for item in all_foiders if os.path.isdir(item)]
    return all_foiders

def get_sound_files(path, extension = "ogg"):
    '''
    '''
    all_items = os.listdir(path)
    all_files = [item for item in all_items if item.endswith(extension)]
    return all_files

def get_data_tag_from_folder_name(folder):
    '''
    '''
    return folder[6:]

def get_features_from_sound_file(source_folder, folder, sound_file):
    path = os.path.join(source_folder, folder, sound_file)
    data, samplerate = sf.read(path)
    return data, samplerate

def write_dataset_to_file(destination_folder, filename, features,tags):
    path = os.path.join(destination_folder, filename)
    h5f = h5py.File(path, "w")
    h5f.create_dataset("sounds", data=features)
    h5f.create_dataset("tags", data=tags)
    h5f.close()


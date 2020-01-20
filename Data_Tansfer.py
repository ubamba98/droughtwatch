#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 13:20:30 2020

@author: debjani

"""

import os
import glob
import matplotlib.pyplot as plt
import numpy as np
import shutil


# get data
base_dir = "/home/debjani/Desktop/droughtwatch1/data/val/"
get_files_path = base_dir + "images_all" + "/*"
training_files = sorted(glob.glob(get_files_path))
label_files_path = base_dir + "label_all/" + "val_labels.txt"
label_file = open(label_files_path)
label_file = label_file.readlines()
#len(label_file)


# make required directory
image_dir_0 = base_dir + "images_all/" + "image_dir_0"
image_dir_1 = base_dir + "images_all/" + "image_dir_1"
image_dir_2 = base_dir + "images_all/" + "image_dir_2"
image_dir_3 = base_dir + "images_all/" + "image_dir_3"
if not os.path.exists(image_dir_0):
            os.mkdir( image_dir_0)
if not os.path.exists(image_dir_1):
            os.mkdir( image_dir_1)
if not os.path.exists(image_dir_2):
            os.mkdir( image_dir_2)
if not os.path.exists(image_dir_3):
            os.mkdir( image_dir_3)
            
            
#transfer files to corresponding folder
for i in range (len(training_files)-1):
    label = label_file[i]
    file = training_files[i]
    if label[6] == "0":
        shutil.move(file, image_dir_0)
    elif label[6] == "1":
         shutil.move(file, image_dir_1)
    elif label[6] == "2":
         shutil.move(file, image_dir_2)
    elif label[6] == "3":
        shutil.move(file, image_dir_3)
    
    
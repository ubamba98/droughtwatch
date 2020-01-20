#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 16:35:03 2019

@author: debjani
"""

import numpy as np
#import get_max_value
import os
import timeit
from glob import glob
from tqdm import tqdm

# number of channels of the dataset image, 4 channels (RGB NIR)

CHANNEL_NUM = 11

def flatten_list(list_of_lists):
    return [val for sublist in list_of_lists for val in sublist]

def cal_dir_stat(root, maximunValue):
    pixel_num = 0 # store all pixel number in the dataset
    channel_sum = np.zeros(CHANNEL_NUM)
    channel_sum_squared = np.zeros(CHANNEL_NUM)

    
    im_pths = glob(root+"/*/*")
    

    for path in tqdm(im_pths):
        im = np.load(path)
        #print(im.shape)
        im = im/maximunValue
        pixel_num += (im.size/CHANNEL_NUM)
        channel_sum += np.sum(im,axis=(0, 1))
        channel_sum_squared += np.sum(np.square(im), axis=(0, 1))
        #print(channel_sum_squared, count)

    rgb_mean = channel_sum / pixel_num
    rgb_std = np.sqrt(channel_sum_squared / pixel_num - np.square(rgb_mean))
    #print(rgb_mean, rgb_std)   
    return rgb_mean, rgb_std


data_path = ''
train_root= 'train'
start = timeit.default_timer() 
#max_val = get_max_value.maxvalue('/home/debjani/Desktop/droughtwatch/data/train/images')
mean, std = cal_dir_stat(train_root, 255)

end = timeit.default_timer()
print("elapsed time: {}".format(end-start))
print("mean:{}\nstd:{}".format(mean, std))
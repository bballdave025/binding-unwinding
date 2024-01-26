#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##############################################################################
# @file: fndtnl_cnn_ms_reuse_clssfctn.py
# @author: Keith PRISBREY        for FamilySearch        principal author
# @author: David BLACK           GH @bballdave025        playing around
#                                                        rewriting for 
#                                                        learning
# @since: 2024-01-25 (for Dave)
#
# (Dave's notes)
#
#  It seems to me that we're using a canned CNN. I dont' know if it is
#  piggybacking off of previous shape recognition, or if it is building
#  up the recognition from scratch. Either way, it will be fun to get
#  results.
#
##############################################################################

import sys, os, time, glob, pickle

from PIL import Image

from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

from sklearn.preprocessing import OneHotEncoder
from sklearn.utils.class_weight import compute_class_weight

import tensorflow as tf
import keras
from keras import backend as K

do_show_progress = True


## Find the number of GPUs
n_gpus = len(tf.config.experimental.list_physical_devices('GPU'))

if do_show_progress:
  print("Number of GPUs: ", str(n_gpus))
##endof:  if do_show_progress


##------------------------------------------
## Define filesystem paths for the dataset
#
# DWB's Windows Setup and the external drive
base_dir_path = "D:/Datasets_and_Models/P2_MSS/DatasetBinding"

if do_show_progress:
  print("base_dir_path: ", base_dir_path)
##endof:  if do_show_progress


## Define paths for each of the classes

#-----------
#   POSITIVE
positive_class_base_dir = os.path.join(base_dir_path, 
                                       "_just_classified_folders",
                                       "__Yes_Reuse"
                          )

if do_show_progress:
  print("positive_class_base_dir:\n", positive_class_base_dir)
##endof:  if do_show_progress

#-----------
#   NEGATIVE
negative_class_base_dir = os.path.join(base_dir_path,
                                       "_just_classified_folders",
                                       "__Not_Reuse"
                          )

if do_show_progress:
  print("negative_class_base_dir:\n", negative_class_base_dir)
##endof:  if do_show_progress


##-------------------------------------------
## FETCH training images for NEGATIVE CLASS
##   we'll call this the "1-class",
##   "not_reused", or "neg"
#

files_for_not_reused = glob.glob(negative_class_base_dir + "*.jpg") + \
                       glob.glob(negative_class_base_dir + "*.png")

print("files_for_not_reused:\n", str(files_for_not_reused))

files_for_yes_reused = glob.glob(positive_class_base_dir + "*.jpg") + \
                       glob.glob(positive_class_base_dir + "*.png")

if do_show_progress:
  print("files_for_yes_reused:\n", str(files_for_yes_reused))
##endof:  if do_show_progress